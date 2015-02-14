#!/usr/bin/env python
import sys
import argparse


class Primes(object):

    def __init__(self, start, howmany, finish):
        if not start == None and start < 2:
            sys.exit("If passing start value, must be >= first prime number of 2.")

        if not start == None:
            self.start = start
        else:
            self.start = 2

        if not howmany == None and howmany < 1:
            sys.exit("If passing howmany value, must be >= 1.")

        if not howmany == None and howmany > 0:
            self.howmany = howmany
        else:
            self.howmany = None

        if not finish == None and finish < 2:
            sys.exit("If passing finish value, must be >= first prime number of 2.")

        if not finish == None:
            self.finish = finish
        else:
            if not howmany == None:
                self.finish = None
            else:
                self.finish = 1000


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
        finish = 15
        col_width = max(len(str(p)) for p in self.primes) + 2
        while start < len(self.primes):
            print "".join(str(p).ljust(col_width) for p in self.primes[start:finish])
            start += 15
            finish += 15
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
