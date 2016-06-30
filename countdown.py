import argparse
import datetime
import time

parser = argparse.ArgumentParser(description="Take in the date we are counting down to")
parser.add_argument("year", type=int)
parser.add_argument("month", type=int)
parser.add_argument("day", type=int)
parser.add_argument("hour", type=int)
parser.add_argument("minute", type=int)
parser.add_argument("-s", help="The scale of the printed output", default='d', choices=['s', 'm', 'h', 'd'])
parser.add_argument("-t", help="Number of seconds between coundown updates", default=1, type=int)
args = parser.parse_args()

while(1):
    now = datetime.datetime.today()
    then = datetime.datetime(args.year, args.month, args.day, args.hour, args.minute)
    delta = then-now
    if args.s == 's':
        seconds = delta.days*24*60*60+delta.seconds
        print str(seconds) + " SECONDS"
    elif args.s == 'm':
        minutes = delta.days*24*60 + delta.seconds/60
        seconds = delta.seconds % 60
        print str(minutes) + " MINUTES " + "{0:2d}".format(seconds) + " SECONDS"
    elif args.s == 'h':
        hours = delta.days*24 + delta.seconds/3600
        minutes = (delta.seconds % 3600) / 60
        seconds = delta.seconds % 60
        print str(hours) + " HOURS " + "{0:2d}".format(minutes) + " MINUTES " + "{0:2d}".format(seconds) + " SECONDS"
    elif args.s == 'd':
        days = delta.days
        hours = delta.seconds / 3600
        minutes = (delta.seconds % 3600) / 60
        seconds = delta.seconds % 60
        print str(days) + " DAYS " + "{0:2d}".format(hours) + " HOURS " + "{0:2d}".format(minutes) + " MINUTES " + "{0:2d}".format(seconds) + " SECONDS"
    time.sleep(args.t)
