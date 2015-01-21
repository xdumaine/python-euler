#!/usr/bin/python

import mathUtils

import sys

if(len(sys.argv) < 2):
    print("Pass in an argument to check")
    quit()

num = int(sys.argv[1])

print(mathUtils.largestPrimeFactor(num))
