import argparse

parser = argparse.ArgumentParser(description="Calculate yield after n years of an interest rate x compounded annually")
parser.add_argument("interest", type=float)
parser.add_argument("years", type=int)
args = parser.parse_args()
intr = args.interest
years = args.years
value = pow(1+intr, years)
print "Assuming all returns are reinvested..."
print "After " + str(years) + " years at " + str(intr*100) + "% interest, your money will be multiplied by: " + str(value) + "x"
