#!/bin/python3

from analyzer.get_files import get_files
from analyzer.parse import parse, find_entries
from analyzer.print_results import print_results
import argparse

parser = argparse.ArgumentParser(
    description='Find logs according to the given parameters. By default it prints the first 300 symbols'
)
parser.add_argument('file', help='Path to file or directory')
parser.add_argument('-d', '--date', help='Datetime for search:\n less than: "../2022-01-13 00:00:00.000",\nmore than: "2022-01-13 00:00:00.000/..",\nfrom - to "2022-01-13 00:00:00.000/2022-01-14 00:00:00.000",\nexact: "2022-01-13 00:00:00.000"')
parser.add_argument('-t', '--text', help='A text to look for')
parser.add_argument('-n', '--unwanted', help='A text to filter out logs. Logs with this text will be excluded from the results. Can be a string or a list divided by commas (e.g. "out of memory, info")')
parser.add_argument('-q', '--symbols_qty', help='How much symbols should be returned. Default is 300', default=300)
parser.add_argument('--full', help='Return full log entry instead of default symbols Qty', action="store_true")
options = parser.parse_args()
# print(options)


if __name__ == '__main__':
    logs = get_files(options.file)
    log_entries = parse(logs)
    filtered_logs = dict()
    len_log_entries = 0
    for log_entry in log_entries:
        filtered_log = find_entries(log_entry, options.text, options.unwanted, options.date)
        filtered_logs.update(filtered_log)
        len_log_entries += len(log_entry)
    print_results(filtered_logs, options.full, options.text, len_log_entries, int(options.symbols_qty))
