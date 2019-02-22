# AMP4e Events
AMP For Endpoints python script to ingest AMQP messages to a local log file. This was originally setup for Sumo Logic, but can be used for other SIEMs. My goal is to make this script as simple as possible, so all you need to do is enter in a few variables to get going.

## Prerequisites
Four variables need to be input at the beginning of the script for this to work:

CLIENT_ID = ''

API_KEY = ''

AMQP_PW = ''

EVENT_STREAM_NAME = ''

## Setup
-Create an API account through the Cisco AMP For Enpoints Admin dashboard to get the ID and Key variables

-To get the AMQP password and event stream name, you will need to create an event stream with Cisco's API of the events you would like to log. Documetation on that can be found at Cisco's site: https://api-docs.amp.cisco.com/api_actions/details?api_action=POST+%2Fv1%2Fevent_streams&api_host=api.amp.cisco.com&api_resource=EventStream&api_version=v1
I personally use Postman to query the API and POST the event stream name, but you can do it whichever way you prefer. 

For example, to get all possible events in an Event Stream called AMP_Logs, this would be the POST URL that would be used:

https://api.amp.cisco.com/v1/event_streams?event_type[]=553648130&event_type[]=554696714&event_type[]=554696715&event_type[]=1091567628&event_type[]=2165309453&event_type[]=1090519054&event_type[]=553648143&event_type[]=2164260880&event_type[]=570425394&event_type[]=553648149&event_type[]=2164260884&event_type[]=2181038130&event_type[]=553648152&event_type[]=2164260889&event_type[]=553648151&event_type[]=553648154&event_type[]=553648155&event_type[]=2164260892&event_type[]=2164260893&event_type[]=553648158&event_type[]=2164260895&event_type[]=553648166&event_type[]=2164260903&event_type[]=1003&event_type[]=1004&event_type[]=1005&event_type[]=2164260866&event_type[]=553648146&event_type[]=553648147&event_type[]=553648168&event_type[]=553648150&event_type[]=570425396&event_type[]=570425397&event_type[]=570425398&event_type[]=570425399&event_type[]=1090524040&event_type[]=1090524041&event_type[]=1090519084&event_type[]=1107296257&event_type[]=1107296258&event_type[]=1107296261&event_type[]=1107296262&event_type[]=1107296263&event_type[]=1107296264&event_type[]=1107296266&event_type[]=1107296267&event_type[]=1107296268&event_type[]=1107296269&event_type[]=1107296270&event_type[]=1107296271&event_type[]=1107296272&event_type[]=1107296273&event_type[]=553648170&event_type[]=553648171&event_type[]=1107296274&event_type[]=1107296275&event_type[]=1107296276&event_type[]=553648173&event_type[]=2164260910&event_type[]=554696756&event_type[]=554696757&event_type[]=1091567670&event_type[]=2165309495&event_type[]=2164260914&event_type[]=553648179&event_type[]=2164260911&event_type[]=553648176&event_type[]=1090519089&event_type[]=1107296277&event_type[]=1107296278&event_type[]=1107296279&event_type[]=1107296280&event_type[]=1107296281&event_type[]=1107296282&event_type[]=1090519096&event_type[]=1090519097&event_type[]=2164260922&event_type[]=553648137&event_type[]=553648135&event_type[]=553648136&event_type[]=1107296285&event_type[]=1107296284&event_type[]=1107296283&event_type[]=1090519103&event_type[]=2164260931&event_type[]=1090519107&event_type[]=553648195&event_type[]=553648196&event_type[]=1090519081&event_type[]=1090519105&event_type[]=1090519102&event_type[]=553648199&event_type[]=1090519112&name=AMP_Logs

## Updates
-Current script works, but connection drops if there are no new events within a certain period of time. Working on getting logic into the script to automatically restart connection if it drops.
