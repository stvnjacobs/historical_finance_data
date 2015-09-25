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

def convert_interval(interval_string):
    if interval_string == 'weekly' or interval_string == 'w':
        return 'w'
    elif interval_string == 'monthly' or interval_string == 'm':
        return 'm'
    elif interval_string == 'dividends' or interval_string == 'v':
        return 'v'
    else:
        return 'd'

@click.command()
@click.option('-i', '--interval', default='daily', prompt='Inteval',
              type=click.Choice(['d', 'daily', 'w', 'weekly', 'm', 'monthly', 'v', 'dividends']),
              help='Available options are "daily" or "d", "weekly" \
              or "w", "monthly" or "m", and lastly "dividends" or "v"')
@click.argument('ticker')

def run(ticker, interval):
    """Simple program that outputs a csv of historical ticker data"""

    interval = convert_interval(interval)

    payload = {
        's': ticker,      # ticker symbol
        'c': '',          # start year
        'a': '',          # start month - 1
        'b': '',          # start day
        'f': '',          # to year
        'd': '',          # to month - 1
        'e': '',          # to day
        'g': interval     # interval
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
