#!/usr/bin/python

import argparse
import requests
import os.path

# command line parser

parser = argparse.ArgumentParser()
parser.add_argument("ticker", help="ticker symbol to be used")
args = parser.parse_args()

ticker = args.ticker

# load parameters into payload for request

payload = {
	's': ticker, # ticker symbol
	'c': '',     # start year
	'a': '',     # start month - 1
	'b': '',     # start day
	'f': '',     # to year
	'd': '',     # to month - 1
	'e': '',     # to day
	'g': 'd'     # interval
	               # d = daily
                   # w = weekly
                   # m = monthly
                   # v = dividends only
}

# set request

r = requests.get('http://ichart.yahoo.com/table.csv', params=payload)


# construct a csv file a csv file

def create_csv(ticker_symbol):

	# csv files will be written in data directory

	subdirectory = 'data'

	# see if data directory exists. if it does not, create one.

	try:
		os.mkdir(subdirectory)
	except Exception:
		pass

	# open/create file. name file by ticker symbol. write and close.

	csv_file = ticker + '.csv'
	
	f = open(os.path.join(subdirectory, csv_file),'wb')
	f.write(r.text)
	f.close

# make sure request is valid and run through create_csv(ticker)

if r.status_code == 200:
	create_csv(ticker)
else:
	print "Something didn't go as planned.  Check your ticker symbol."


