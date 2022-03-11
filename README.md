# Logs Analyzer
## Installation
```commandline
pip install -r requirements.txt
```
## Usage
```
python3 analyze.py [-h] [-d DATE] [-t TEXT] [-n UNWANTED] [--full FULL] file
```

Find logs according to the given parameters. Text search is case-insensitive. By default, it prints the first
300 symbols

positional arguments:  
  file                  Path to file or directory 

optional arguments:  
  -h, --help:            show help message and exit  
  -d DATE, --date DATE:  Datetime for search: less than: "../2022-01-13
                        00:00:00.000", more than: "2022-01-13
                        00:00:00.000/..", from - to "2022-01-13
                        00:00:00.000/2022-01-14 00:00:00.000", exact:
                        "2022-01-13 00:00:00.000"  
  -t TEXT, --text TEXT:  A text to look for (case-insensitive)  
  -n UNWANTED, --unwanted UNWANTED:
                        A text to filter out logs. (case-insensitive) Logs with this text will
                        be excluded from the results. Can be a string or a
                        list divided by commas (e.g. "out of memory, info")   
  -q SYMBOLS_QTY, --symbols_qty SYMBOLS_QTY: How much symbols should be returned. Default is 300  
  --full                Return full log entry instead of default symbols Qty  

### Usage example:  
```commandline
python3 analyze.py ../logs/ -t "Sql exception" -n "FunctionError, warning" -d "2022-01-13 11:19:19.642/2022-01-13 11:54:20.189"
```

