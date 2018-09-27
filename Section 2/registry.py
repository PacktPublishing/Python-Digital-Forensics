#!/usr/bin/python3

# SOFTWARE\Microsoft\Windows\CurrentVersion\Run
# Wow6432Node\Microsoft\Windows\CurrentVersion\Run
# Microsoft\Windows NT\CurrentVersion\Winlogon\System

# HKEY_LOCAL_MACHINE

import winreg
import argparse


class RegDemo:
    def __init__(self):
        pass

    @staticmethod
    def get_args():
        """Take a++ look at those args."""
        parser = argparse.ArgumentParser(description='Query the registry')
        parser.add_argument("-e", "--enum", help="Enumerate all keys")
        parser.add_argument("-ev", "--enum-val", help="Enumerate all values")
        parser.add_argument("-q", "--query", nargs=2, help="Query registry value")

        return parser.parse_args()

    def enum(self, hive, reg_path):
        try:
            registry_key = winreg.OpenKey(
                hive, reg_path, 0, winreg.KEY_READ)
            i = 0
            while True:
                value = winreg.EnumKey(registry_key, i)
                print(value)
                i += 1
        except WindowsError as e:
            print("Error Loading key\n{}".format(e))

        finally:
            winreg.CloseKey(registry_key)

    def enum_val(self, hive, reg_path):
        try:
            registry_key = winreg.OpenKey(
                hive, reg_path, 0, winreg.KEY_READ)
            i = 0
            while True:
                value = winreg.EnumValue(registry_key, i)
                print(value)
                i += 1
        except WindowsError as e:
            print("Error Loading key\n{}".format(e))

        finally:
            winreg.CloseKey(registry_key)

    def query(self, hive, reg_path, value_name):
        try:
            registry_key = winreg.OpenKey(
                hive, reg_path, 0, winreg.KEY_READ)

            value = winreg.QueryValueEx(registry_key, value_name)[1]
            print(value)

        except WindowsError as e:
            print("Error Loading key\n{}".format(e))

        finally:
            winreg.CloseKey(registry_key)

    def main(self):
        args = self.get_args()
        hive = winreg.HKEY_CURRENT_USER

        if args.enum:
            self.enum(hive, args.enum)
        if args.enum:
            self.enum_val(hive, args.enum_val)
        if args.query:
            self.query(hive, args.query[0], args.query[1])


if __name__ == '__main__':
    reg_instance = RegDemo()
    reg_instance.main()
