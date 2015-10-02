## Why?

I occasionally need historical stock price information that can easily be parsed for charting and analysis.

## How does it work?

```historical_finance_data.py``` will retrieve historical stock information and save it to a ```.csv``` file.  Information comes from Yahoo Finance, and requests are limited to the information in their database.

### Dependencies

- Python (currently running on [Python 2.7](https://docs.python.org/2/))
- [Virtualenv](https://virtualenv.pypa.io/en/latest/) is recommended.  I recommend reading [The Hitchhikers Guide to Python section on Virtual Environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/) if you are not familiar with Python virtual environments.

### Getting Started

```bash
$ git clone https://github.com/stvnjacobs/historical_finance_data.git
$ cd historical_finance_data
```

Install the necessary dependencies using pip.  (Again, Virtualenv is recommended to isolate dependencies)

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

### Running The Program

The program is run from the command line, and you must provide it with a valid ticker symbol.

_note_: These commands are run from the folder which contains ```historical_finance_data.py```.  The ability to run it from anywhere, or infomration on how to do so, will soon be added.

```bash
$ python historical_finance_data.py VTI
```

If you do not set an interval, you will be prompted to enter one.  The script currently pulls daily data by default.  You also have the option of weekly, monthly, yearly, or only dividend data.  

_note:_ These can all be set from the start as an attribute with the ```-i``` or ```--interval``` flag when you first input the command.

- ```d``` or ```daily``` for daily data.
- ```w``` or ```weekly``` for weekly data.
- ```m``` or ```monthly``` for monthly data.
- ```v``` or ```dividends``` will return all dividend payouts.

The newly created ```.csv``` file will be placed in a ```data``` directory.  If you were to get information for VTI, the Vanguard Total Stock Market ETF, the resulting file tree of the directory will look something like this:

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
-  Setuptools integration ([Instructions](http://click.pocoo.org/5/setuptools/#setuptools-integration))
-  Option to create chart
