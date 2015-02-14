# Prime Number Generator
Python script for printing out prime numbers.

Install/Run Steps:
- Install requirements/system.txt (sudo apt-get install python), etc
- Install needed python modules (sudo pip install -r requirements/python.txt)
- Run script (./bin/primes.py), optionally with:
  - (-f | --finish) to pass a custom upper limit integer
  - (-s | --start) to pass a custom starting integer
  - (-m | --howmany) to pass number of primes desired returned.

Note: If both (-f | --finish) and (-m | --howmany) are passed, it script will terminate at whichever limit is reached first.

Sample Commands from project scope:

| Command | Description |
|:--------|:------------|
| ```./bin/python.py``` | Returns all primes from 0 - 1000 by default |
| ```./bin/python.py -f 10000``` | Returns all primes from 0 - 10000 |
| ```./bin/python.py -s 50 -f 100``` | Returns all primes between 50 - 100 |
| ```./bin/python.py -m 1000``` | Returns first 1000 prime numbers starting from 0 |
| ```./bin/python.py -m 10 > samples/first_10.txt``` | Returns first 10 prime numbers into output file. |
