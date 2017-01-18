import requests
import json
from time import strftime, localtime
from configspy import location
from configspy import api_key
from operator import itemgetter


#map = {'H':'high','L':'low'}
#print map['H']
tidespy_url = 'http://tidespy.com/api/tideturns?'
unit = 'm'
days = '3'
debug = 1
request_url = tidespy_url + 'pn=' + location + '&unit=' + unit + '&start=' + strftime("%Y%m%d", localtime()) + '&days=' + days + '&key=' + api_key
if debug == 1:
  print request_url
tidejson = requests.get(request_url).text
if debug == 1:
  print tidejson 
tidedict = json.loads(tidejson)
if debug == 1:
  print tidedict 
turns = tidedict['Turns']
if debug == 1:
  print turns 

def datestring (date, minutes):
  "Returns date string YYYYMMDDHHMM from date and minutes into day"
  return date + str(("{:02}".format(minutes/60))) + str(("{:02}".format(minutes%60)))
  
#print datestring ('20170112', 345)



turns = sorted(turns, key = itemgetter ('Date','Minute'))

if debug == 1:
  print "There are originally  " + str(len (turns)) + " items\n"
for i in range (len (turns) - 1, -1, -1):
  if (datestring(turns[i]['Date'],turns[i]['Minute'] + 390) < strftime("%Y%m%d%H%M", localtime())):
    print ("Will delete" + str(i))
    del turns[i]

print "\nShortened turns = " + str(turns) + "\n"
print "There are now  " + str(len (turns)) + " items\n"


tidesfile = open('/home/nick/Downloads/TideTimes/tides','w')
tidesfile.write(str(tidedict))
tidesfile.close()

turnsfile = open('/home/nick/Downloads/TideTimes/turns','w')
turnsfile.write(str(turns))
turnsfile.close()
