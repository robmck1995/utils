import argparse
import datetime
import time

pay = 27.5

parser = argparse.ArgumentParser()
parser.add_argument("pay_rate", type=float)
parser.add_argument("in_hour", type = int)
parser.add_argument("in_minute", type=int)
parser.add_argument("time_so_far", type=float)
args = parser.parse_args()
while(1):
    now = datetime.datetime.today()
    clock_in = datetime.datetime(now.year, now.month, now.day, args.in_hour, args.in_minute)
    time_worked = (now-clock_in+datetime.timedelta(seconds=args.time_so_far*3600)).seconds/3600.0
    reg_hours = 8 if time_worked >= 8 else time_worked
    over_hours = time_worked - 8 if time_worked > 8 else 0
    over_hours = 4 if over_hours > 4 else over_hours
    double_hours = time_worked - 12 if time_worked > 12 else 0
    pay_hours = reg_hours + 1.5*over_hours + 2*double_hours
    print "Hours: " + "{0:.3f}".format(reg_hours+over_hours+double_hours) + ", Comp: $" + "{0:.2f}".format(pay_hours*pay)
    time.sleep(1)
