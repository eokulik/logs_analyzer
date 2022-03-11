from colorama import Fore




def print_results(log_entries: dict, full: bool, text: str, total_logs_count: int, symbols_qty: int):
    for entry_date, entry_log in log_entries.items():
        if full:
            print(entry_log)
        else:
            if text:
                text_before = (
                    entry_log[entry_log.find(text) - symbols_qty // 2: entry_log.find(text)] if len(entry_log[: entry_log.find(text)]) > symbols_qty // 2 else entry_log[: entry_log.find(text)]
                )
                text_after = (
                    entry_log[entry_log.find(text) + len(text): entry_log.find(text) + len(text) + symbols_qty // 2] if len(entry_log[entry_log.find(text) + len(text):]) > symbols_qty // 2 else entry_log[entry_log.find(text) + len(text):]
                )
                print(
                    '[{0}]'.format(Fore.YELLOW + str(entry_date) + Fore.RESET),
                    '{0}{1}{2}'.format(
                        text_before,
                        # entry_log[entry_log.find(text) - 15: entry_log.find(text)],
                        Fore.GREEN + entry_log[entry_log.find(text): entry_log.find(text) + len(text)] + Fore.RESET,
                        text_after
                        # entry_log[entry_log.find(text) + len(text): entry_log.find(text) + len(text) + 150]
                    )
                )
            else:
                print(
                    '[{0}]'.format(Fore.GREEN + str(entry_date) + Fore.RESET),
                    entry_log[:symbols_qty]
                )
    print(Fore.YELLOW + 'Total logs count:', Fore.CYAN + str(total_logs_count), Fore.RESET)
    print(Fore.YELLOW + 'Total results count:', Fore.CYAN + str(len(log_entries)), Fore.RESET)
