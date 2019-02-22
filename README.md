# AMP4e Events
AMP For Endpoints python script to ingest AMQP messages to a local log file. This was originally setup for Sumo Logic, but can be used for other SIEMs.

## Prerequisites
Four variables need to be input at the beginning of the script for this to work:

CLIENT_ID = ''

API_KEY = ''

AMQP_PW = ''

event_stream_name = ''

## Setup
-Create an API account through the Cisco AMP For Enpoints Admin dashboard to get the ID and Key variables

-To get the AMQP password and event stream name, you will need to create an event stream with Cisco's API of the events you would like to log. Documetation on that can be found at Cisco's site: https://api-docs.amp.cisco.com/api_actions/details?api_action=POST+%2Fv1%2Fevent_streams&api_host=api.amp.cisco.com&api_resource=EventStream&api_version=v1
I personally use Postmasn to query the API and POST the event stream name, but you can do it whichever way you prefer.

## Updates
-Current script works, but connection drops if there are no new events within a certain period of time. Working on getting logic into the script to automatically restart connection if it drops.
