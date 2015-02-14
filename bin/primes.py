#!/usr/bin/env python
import argparse


class Primes(object):

    def __init__(self, limit):
        if not limit == None:
            self.limit = limit
        else:
            self.limit = 100000
        return

    def run(self):
        num = 2
        while num <= self.limit:
            div = 2
            stat = True
            while div < num:
                if num % div == 0:
                    stat = False
                div += 1
            if stat == True:
                print num
            num += 1
        return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--limit", type=int, help="Override default Limit of 100,000.")
    args = parser.parse_args()
    Primes(limit=args.limit).run()
