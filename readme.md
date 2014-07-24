## Why?

Need historical stock price information, with the added bonus of volume, daily highs and lows.

## How does it work?

```historical_finance_data.py``` will retreive historical stock information and save the information to a ```.csv``` file.  Information comes from yahoo finance, and requests are limited to the information in their database.

It currently pulls daily data.  For weekly, monthly, yearly, or only dividends, see ```payload {...}``` comments for these parameters.

### Dependencies

- python (currently running on [Python 2.7.6](https://docs.python.org/2/))
- requests ([installation docs](http://docs.python-requests.org/en/latest/user/install/)) 

### Running the program

Clone the repository.

```
git clone https://github.com/stvnjacobs/historical_finance_data.git
```

Move into the newly cloned directory.

```
cd historical_finance_data
```

Run the command with a valid ticker symbol.

```
python historical_finance_data.py VTI
```

Newly created ```.csv``` files will be placed in ```data``` directory

```
historical_finance_data
├── data
│   └── VTI.csv
├── .gitignore
├── historical_finance_data.py
└── readme.md

```

Here is what the first 10 lines of the ```VTI.csv``` we just created (on April 29th, 2014) looks like.

```
head -10 data/VTI.csv
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

-  more command line arguments for refining output
-  outputting chart in svg and image formats
