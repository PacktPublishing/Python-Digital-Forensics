#!/usr/bin/python3


from systemd import journal


class LogParse:
    def __init__(self):
        self.j = journal

    def main(self):
        self.j.send("Hello World! Again!")
        self.j.send('Hello, again, world', FIELD2='Greetings!', FIELD3='Guten tag')
        self.j.send('Binary message', BINARY=b'\xde\xad\xbe\xef')



if __name__ == '__main__':
    log_instance = LogParse()
    log_instance.main()
