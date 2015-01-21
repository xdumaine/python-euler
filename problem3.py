#!/usr/bin/python

import sys

def isPrime(num):
    if num < 2 or num % 2 == 0:
        return num == 2
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

if(len(sys.argv) < 2):
    print("Pass in an argument to check")
    quit()

num = int(sys.argv[1])

if isPrime(num):
    print(num)
    quit()

i = 3
while i < num / 2 + 1:
    if num % i == 0:
        f = num / i
        if isPrime(f):
            print(f)
            quit()
    i += 1
