import sys
import os


class Logger(object):
    """
    Lumberjack class - duplicates sys.stdout to a log file and it okay
    source: /questions/49207/how-do-i-duplicate-sysstdout-to-a-log-file-in-python/348798#348798
    """
    def __init__(self, filename="Red.Wood", mode="a"):
        self.stdout = sys.stdout
        self.file = open(filename, mode)
        sys.stdout = self

    def __del__(self):
        self.close()

    def __enter__(self):
        pass

    def __exit__(self, *args):
        pass

    def write(self, message):
        self.stdout.write(message)
        self.file.write(message)

    def flush(self):
        self.stdout.flush()
        self.file.flush()
        os.fsync(self.file.fileno())

    def close(self):
        if self.stdout is not None:
            sys.stdout = self.stdout
            self.stdout = None

        if self.file is not None:
            self.file.close()
            self.file = None
