#!/usr/bin/python3

# https://eli.thegreenplace.net/2011/12/27/python-threads-communication-and-stopping

import os
import argparse
import threading
import queue


class RecursiveProbe(threading.Thread):
    def __init__(self, dir_q, result_q):
        super(RecursiveProbe, self).__init__()
        self.dir_q = dir_q
        self.result_q = result_q
        self.stoprequest = threading.Event()

    def run(self):
        while not self.stoprequest.isSet():
            try:
                dirname = self.dir_q.get(True, 0.05)
                filenames = list(self._files_in_dir(dirname))
                self.result_q.put((self.name, dirname, filenames))

            except queue.Empty:
                continue

    def join(self, timeout=None):
        self.stoprequest.set()
        super(RecursiveProbe, self).join(timeout)

    def _files_in_dir(self, dirname):
        """ Given a directory name, yields the names of all files (not dirs)
            contained in this directory and its sub-directories.
        """
        for path, dirs, files in os.walk(dirname):
            for file in files:
                # Gives full file path
                yield os.path.join(path, file)


class DirectoryWalk:
    def __init__(self):
        self.path = '.'

    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser(description="Scan all magic files")
        parser.add_argument("path", help="Path to top level directory")

        return parser.parse_args()

    def main(self):
        args = self.get_args()
        self.path = args.path

        # Create a single input and a single output queue for all threads.
        dir_q = queue.Queue()
        result_q = queue.Queue()

        # Create the "thread pool"
        pool = [RecursiveProbe(
            dir_q=dir_q, result_q=result_q) for i in range(4)]

        # Start all threads
        for thread in pool:
            thread.start()

        # Give the workers some work to do
        if os.path.exists(self.path):
            dir_q.put(self.path)

        # Now get all the results
        work_count = 1
        while work_count > 0:
            # Blocking 'get' from a Queue.
            result = result_q.get()
            print(result)
            print('From thread {0}: {1} files found in dir {2}'.format(
                result[0], len(result[2]), result[1]))

            work_count -= 1

        # Ask threads to die and wait for them to do it
        for thread in pool:
            thread.join()


if __name__ == '__main__':
    walk_instance = DirectoryWalk()
    walk_instance.main()
