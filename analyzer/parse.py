from datetime import datetime


def parse(logs: list) -> dict:
    date = None
    entries = {}
    for log in logs:
        for line in log:
            possible_date = line[:23]
            try:
                date = datetime.strptime(possible_date, '%Y-%m-%d %H:%M:%S.%f')  # 2022-01-13 12:34:20.517
                entries[date] = line
            except ValueError:
                if date:
                    entries[date] += line
                continue
    return entries


def find_entries(log_entries: dict, text: str, unwanted: str, date: str) -> dict:
    if date:
        if date.startswith('..'):
            date = datetime.strptime(date[3:], '%Y-%m-%d %H:%M:%S.%f')
            log_entries = dict((key, value) for key, value in log_entries.items() if key <= date)

        elif date.endswith('..'):
            date = datetime.strptime(date[:-3], '%Y-%m-%d %H:%M:%S.%f')
            log_entries = dict((key, value) for key, value in log_entries.items() if key >= date)
        elif '/' in date:
            date_1 = datetime.strptime(date[:date.find('/')], '%Y-%m-%d %H:%M:%S.%f')
            date_2 = datetime.strptime(date[date.find('/') + 1:], '%Y-%m-%d %H:%M:%S.%f')
            log_entries = dict((key, value) for key, value in log_entries.items() if date_1 <= key <= date_2)
        else:
            date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
            log_entries = dict((key, value) for key, value in log_entries.items() if key == date)
    if text:
        log_entries = dict((key, value) for key, value in log_entries.items() if text.lower() in value.lower())
    if unwanted:
        if ',' in unwanted:
            unwanted = unwanted.split(',')
        else:
            unwanted = [unwanted]
        for unw in unwanted:
            log_entries = dict((key, value) for key, value in log_entries.items() if unw.strip().lower() not in value.lower())
    return log_entries

