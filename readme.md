## Why?

Needed historical stock price information, with the added bonus of volume, daily highs and lows.

## How does it work?

```historical_finance_data.py``` will retreive historical stock information and save the information to a ```.csv``` file.  Information comes from Yahoo Finance, and requests are limited to the information in their database.

It currently pulls daily data.  For weekly, monthly, yearly, or only dividends, see ```payload {...}``` comments for these parameters.

### Dependencies

- Python (currently running on [Python 2.7.6](https://docs.python.org/2/))
- [Virtualenv](https://virtualenv.pypa.io/en/latest/) is recommended

### Getting Started

```bash
$ git clone https://github.com/stvnjacobs/historical_finance_data.git
$ cd historical_finance_data
```

Install the necessary dependencies using pip.  (Again, Virtualenv is recommended to isolate dependencies)

```bash
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### Running The Program
Run the command with a valid ticker symbol.

```bash
$ python historical_finance_data.py VTI
```

Currently there are options for intervals of data which can be found by running the ```--help``` argument.

```bash
$ python historical_finance_data.py --help

Usage: historical_finance_data.py [OPTIONS] TICKER

  Simple program that outputs a csv of historical ticker data

Options:
  -i, --interval [d|daily|w|weekly|m|monthly|v|dividends]
                                  Available options are "daily" or "d",
                                  "weekly" or "w", "monthly" or
                                  "m", and lastly "dividends" or "v"
  --help                          Show this message and exit.
```

Newly created ```.csv``` files will be placed in ```data``` directory

```
historical_finance_data
├── data
│   └── VTI.csv
├── historical_finance_data.py
└── readme.md
```

Here is what the first 10 lines of the ```VTI.csv``` we just created (on April 29th, 2014) looks like.

```bash
$ head -10 data/VTI.csv
```

```
Date,Open,High,Low,Close,Volume,Adj Close
2014-04-28,96.90,97.22,95.65,96.69,2046000,96.69
2014-04-25,97.19,97.25,96.34,96.55,1927700,96.55
2014-04-24,97.84,97.90,96.96,97.50,1471400,97.50
2014-04-23,97.62,97.68,97.30,97.37,1798400,97.37
2014-04-22,97.26,97.91,97.19,97.62,2442400,97.62
2014-04-21,96.78,97.12,96.57,97.12,3043000,97.12
2014-04-17,96.42,96.97,96.26,96.73,2241100,96.73
2014-04-16,96.21,96.55,95.75,96.54,4498500,96.54
2014-04-15,95.13,95.60,94.03,95.54,3339400,95.54
```

## Taking it further

-  Add more command line arguments for refining output:
	- [x] Intervals & Dividends
	- [ ] Date ranges and deltas
-  Option to create chart
