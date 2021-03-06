#!/usr/bin/env python
import os
import sys
import time
import dotenv
import argparse
import logging
import logging.config

dotenv.read_dotenv(os.path.dirname(os.path.realpath(__file__)) + '/../.env')
logging.config.fileConfig('logging.conf', defaults={'logfilename': 'logs/primes.log'})

if os.environ['START']:
    START = int(os.environ['START'])
else:
    START = 2

if os.environ['FINISH']:
    FINISH = int(os.environ['FINISH'])
else:
    FINISH = 1000

if os.environ['HOW_MANY']:
    HOW_MANY = int(os.environ['HOW_MANY'])
else:
    HOW_MANY = None

if os.environ['COLUMN_PADDING']:
    COLUMN_PADDING = int(os.environ['COLUMN_PADDING'])
else:
    COLUMN_PADDING = 2

if os.environ['HOW_MANY_PER_ROW']:
    HOW_MANY_PER_ROW = int(os.environ['HOW_MANY_PER_ROW'])
else:
    HOW_MANY_PER_ROW = 15


class Primes(object):

    def __init__(self, start, howmany, finish):
        self.start_time = time.time()
        self.logger = logging.getLogger('primes')

        if not start == None and start < START:
            self.logger.error("If passing start value, must be >= first prime number of 2.")
            sys.exit(0)

        if not start == None:
            self.start = start
        else:
            self.start = START

        if not howmany == None and howmany < 1:
            self.logger.error("If passing howmany value, must be >= 1.")
            sys.exit(0)

        if not howmany == None and howmany > 0:
            self.howmany = howmany
        else:
            self.howmany = HOW_MANY

        if not finish == None and finish < START:
            self.logger.error("If passing finish value, must be >= first prime number of 2.")
            sys.exit(0)

        if not finish == None:
            self.finish = finish
        else:
            if not howmany == None:
                self.finish = None
            else:
                self.finish = FINISH

        self.primes = []
        return

    def run(self):
        num = self.start

        if not self.finish == None:
            while num <= self.finish:
                div = 2
                stat = True
                while div < num:
                    if num % div == 0:
                        stat = False
                    div += 1
                if stat == True:
                    self.primes.append(num)
                    if not self.howmany == None:
                        if len(self.primes) == self.howmany:
                            return
                num += 1

        else:
            while len(self.primes) < self.howmany:
                div = 2
                stat = True
                while div < num:
                    if num % div == 0:
                        stat = False
                    div += 1
                if stat == True:
                    self.primes.append(num)
                num += 1

        return

    def out(self):
        start = 0
        finish = HOW_MANY_PER_ROW
        col_width = max(len(str(p)) for p in self.primes) + COLUMN_PADDING
        while start < len(self.primes):
            primes_row = "".join(str(p).ljust(col_width) for p in self.primes[start:finish])
            print primes_row
            self.logger.info(primes_row)
            start += HOW_MANY_PER_ROW
            finish += HOW_MANY_PER_ROW
        return

    def get_elapsed(self):
        finish = time.time()
        elapsed = (finish - self.start_time)
        elapsed_str = 'Elapsed Time: {0} seconds'.format(elapsed)
        print elapsed_str
        self.logger.info(elapsed_str)
        return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--start", type=int, help="Start counting primes from this number. Default is first prime 2.")
    parser.add_argument("-f", "--finish", type=int, help="This is upper limit for counting primes, ie primes whose value is <= this limit. Default is 1,000.")
    parser.add_argument("-m", "--howmany", type=int, help="How many primes do you want? (If both -f and -n are passed, whichever limit is reached first.)")
    args = parser.parse_args()

    primes = Primes(start=args.start,
                    howmany=args.howmany,
                    finish=args.finish)
    primes.run()
    primes.out()
    primes.get_elapsed()
