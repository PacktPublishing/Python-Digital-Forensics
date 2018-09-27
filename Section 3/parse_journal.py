#!/usr/bin/python3

# https://github.com/systemd/python-systemd

from systemd import journal


class LogParse:
    def __init__(self):
        self.journal_reader = journal.Reader()

    def main(self):
        self.journal_reader.this_boot()
        for event in self.journal_reader:
            if event['MESSAGE'] == "Hello World! Again!":
                print(event['MESSAGE'])


if __name__ == '__main__':
    log_instance = LogParse()
    log_instance.main()
