import sys

debug = 0

arg = sys.argv[1]

map = {'H':'High', 'L':"Low"}

tidesfile = open('/home/nick/Downloads/TideTimes/tides','r')
tides = eval(tidesfile.read())
tidesfile.close()
if debug == 1:
  print tides
turnsfile = open('/home/nick/Downloads/TideTimes/turns','r')
turns = eval(turnsfile.read())
turnsfile.close()
if debug == 1:
  print turns


if arg == 'location':
  print "Tides at " + tides["Name"]
elif arg == 'tide0':
  print  map[turns[0]["HorL"]] + " at " + str(("{:02}".format(turns[0]["Minute"]/60))) + ":" + str(("{:02}".format(turns[0]["Minute"]%60)))
elif arg == 'height0':
  print turns[0]["Height"]
elif arg == 'tide1':
  print  map[turns[1]["HorL"]] + " at " + str(("{:02}".format(turns[1]["Minute"]/60))) + ":" + str(("{:02}".format(turns[1]["Minute"]%60)))
elif arg == 'height1':
  print turns[1]["Height"]
elif arg == 'tide2':
  print  map[turns[2]["HorL"]] + " at " + str(("{:02}".format(turns[2]["Minute"]/60))) + ":" + str(("{:02}".format(turns[2]["Minute"]%60)))
elif arg == 'height2':
  print turns[2]["Height"]


