#!/usr/bin/python3


import os
import argparse
from termcolor import cprint
import hashlib


class HashFile:
    def __init__(self):
        self.path = None

    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser(description="Scan all magic files")
        parser.add_argument("path", help="Path to top level directory")
        parser.add_argument("-c", "--compare", help="Provide a hash or hash" +
                            "file to compare")

        return parser.parse_args()

    def open_hash(self, hash_path):
        hash = hash_path
        if os.path.isfile(hash_path):
            with open(hash_path, 'r') as f:
                hash = f.read().splitlines()[0]

        return hash

    def compare_hash(self, old, new):
        if old == new:
            cprint("> Computation complete {}".format(old), 'green')
        else:
            cprint("> DIGEST MISMATCH\nold {0}\nnew {1}".format(
                old, new), 'red')

    def hash_file(self, file):
        BUFF_SIZE = 65536
        digest = hashlib.sha1()

        cprint("> Computing message digest of image", 'blue')
        with open(file, 'rb') as f:
            while True:
                data = f.read(BUFF_SIZE)
                if not data:
                    break
                digest.update(data)
        hash = digest.hexdigest()

        return hash

    def main(self):
        args = self.get_args()
        self.path = args.path

        hash = self.hash_file(self.path)

        if args.compare:
            old_hash = self.open_hash(args.compare)
            self.compare_hash(old_hash, hash)
        else:
            cprint("> Computation Complete \n{}".format(hash), 'green')


if __name__ == '__main__':
    hash_instance = HashFile()
    hash_instance.main()
