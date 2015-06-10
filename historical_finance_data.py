#!/usr/bin/python

import requests
import os.path
import click

subdirectory = 'data'

def create_directory():
    try:
        os.mkdir(subdirectory)
    except Exception:
        pass

def create_csv(ticker, response):
    csv_file = ticker + '.csv'

    f = open(os.path.join(subdirectory, csv_file),'wb')
    f.write(response)
    f.close

@click.command()
@click.option('--ticker', prompt='Ticker symbol',
              help='Ticker symbol to look up.')
def run(ticker):
    """Simple program that outputs a csv of historical ticker data"""
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

    r = requests.get('http://ichart.yahoo.com/table.csv', params=payload)

    if r.status_code == 200:
        create_directory()
        create_csv(ticker, r.text)
    else:
        click.echo("Something didn't go as planned.  Check your ticker symbol.")

if __name__ == '__main__':
    run()
