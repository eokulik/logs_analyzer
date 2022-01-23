from colorama import Fore


def print_results(log_entries: dict, full: bool, text: str, total_logs_count: int):
    for entry_date, entry_log in log_entries.items():
        if full:
            print(entry_log)
        else:
            if text:
                print(
                    '[{0}]'.format(Fore.YELLOW + str(entry_date) + Fore.RESET),
                    '{0}{1}{2}'.format(
                        entry_log[entry_log.find(text) - 150: entry_log.find(text)],
                        Fore.GREEN + entry_log[entry_log.find(text): entry_log.find(text) + len(text)] + Fore.RESET,
                        entry_log[entry_log.find(text) + len(text): entry_log.find(text) + len(text) + 150]
                    )
                )
            else:
                print(
                    '[{0}]'.format(Fore.GREEN + str(entry_date) + Fore.RESET),
                    entry_log[:300]
                )
    print(Fore.YELLOW + 'Total logs count:', Fore.CYAN + str(total_logs_count), Fore.RESET)
    print(Fore.YELLOW + 'Total results count:', Fore.CYAN + str(len(log_entries)), Fore.RESET)
