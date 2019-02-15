#!/usr/bin/env python

#This script intakes logs from the Cisco AMP stream and logs them to a local file. Sumo Logic is then pointed to that local file.

import pika
import requests
import logging
import time
from logging import handlers
from logging.handlers import RotatingFileHandler

# YOU NEED TO input the required info into the CLIENT_ID, API_KEY, AMPQ_PW, AND event_stream_name STRINGS
CLIENT_ID = '<redacted>'
API_KEY = '<redacted>'
AMPQ_PW = '<redacted>' 
event_stream_name = '<redacted>' 

#Logging configuration
amp_logger = logging.getLogger('AMPLogger')
amp_logger.setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler('/opt/AMP4e/Logs/AMP4e.log', maxBytes=2000000)
handler = logging.handlers.SysLogHandler(address = '/dev/log')
amp_logger.addHandler(handler)
logging.basicConfig(filename = '/opt/AMP4e/Logs/AMP4e.log', level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s',datefmt='%a, %d %b %Y %H:%M:%S')

#Connect to Cisco AMP API
api_endpoint = 'https://api.amp.cisco.com/v1/event_streams'

session = requests.Session()
session.auth = (CLIENT_ID, API_KEY)

event_streams = session.get(api_endpoint).json()['data']

event_stream = {}

for e in event_streams:
    if e['name'] is event_stream_name:
        event_stream = e

amqp_url = 'amqps://{user_name}:'AMQP_PW'@{host}:{port}'.format(
    **e['amqp_credentials'])
queue = e['amqp_credentials']['queue_name']
parameters = pika.URLParameters(amqp_url)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

parameters = pika.URLParameters(amqp_url)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

def callback(ch, method, properties, body):
    logging.info(" [x] Received meth:\t%r" % method)
    logging.info(" [x] Received prop:\t%r" % properties)
    logging.info(" [x] Received body:\t%r" % body)

channel.basic_consume(callback, queue, no_ack=True)

logging.info(" [*] Connecting to:\t%r" % amqp_url)
logging.info(" [*] Waiting for messages...")
channel.start_consuming()
