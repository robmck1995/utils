import argparse

compounding_map = {"weekly" : 52, "monthly" : 12, "quarterly" : 4, "biannually" : 2}

parser = argparse.ArgumentParser(description="Calculate yield after n years of an interest rate x")
parser.add_argument("interest", type=float)
parser.add_argument("years", type=int)
parser.add_argument("initial_investment", type=float)
parser.add_argument("--recurring", type=float)
parser.add_argument("--period", choices=["weekly", "monthly", "quarterly", "biannually", "annually"], default="annually")
parser.add_argument("--compounding", choices=["weekly", "monthly", "quarterly", "biannually", "annually"], default="annually")
args = parser.parse_args()
intr = args.interest
years = args.years
inital = args.initial_investment
