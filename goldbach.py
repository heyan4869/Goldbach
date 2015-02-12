#!/usr/bin/env python

import sys

# function ifprime(num) check if an interger is a prime
def ifprime(num):
    i = 2
    while i < num:
        if 0 == (num % i):
            return False
        else:
            i = i + 1
    return True

# function primes(n) returns a sorted list of the prime
# numbers that small or equal to n
def primes(n):
    listofprime = []
    for j in range(2, n + 1):
        if(ifprime(j)):
            listofprime.append(j)
    return listofprime

# function sumOfPrimes(k) returns two primes a and b
# with a small or equal to b such that a + b = k, or
# returns 0 if there are no pair of a, b exists
def sumOfPrimes(k):
    listofcan = primes(k)
    lengthoflist = len(listofcan)
    for i in xrange(0, lengthoflist):
        for j in xrange(i, lengthoflist):
            if listofcan[i]+listofcan[j] == k:
                return listofcan[i], listofcan[j]
    return 0

# function allSumOfPrimes(k) returns a list of all pairs
# (a,b) such that a and b are prime, a small or equal to b,
# and a + b = k
def allSumOfPrimes(k):
    listofcan = primes(k)
    lengthoflist = len(listofcan)
    combs = []
    for x in xrange(0, lengthoflist):
        for y in xrange(x, lengthoflist):
            if listofcan[x]+listofcan[y] == k:
                combs.append((listofcan[x], listofcan[y]))
    return combs

# function goldbach(k) tests all the even integers that small
# or equal to k and see whether they can be written as the sum
# of 2 primes
def goldbach(k):
    bool = 1
    listeven = []
    for e in xrange(3, k+1):
        if e%2 == 0:
            listeven.append(e)
    lengthofeven = len(listeven)

    triple = []
    for m in xrange(0, lengthofeven):
        combs = allSumOfPrimes(listeven[m])
        lengthofcombs = len(combs)
        if lengthofcombs == 0:
            bool = 0
        for n in xrange(lengthofcombs-1, lengthofcombs):
            a, b = combs[n]
            triple.append((listeven[m], a, b))
    lengthoftriple = len(triple)
    if bool == 1:
        return triple, True
    else:
        return triple, False

# function goldbachWidth(k) that returns a dictionary (map)
# D such that D[z] is the number of ways each even number
# z that large than 2 and small or equal to k can be written
# as the sum of two primes
def goldbachWidth(k):
    listeven = []
    for e in xrange(3, k+1):
        if e%2 == 0:
            listeven.append(e)
    lengthofeven = len(listeven)

    dic = []
    for m in xrange(0, lengthofeven):
        combs = allSumOfPrimes(listeven[m])
        lengthofcombs = len(combs)
        dic.append((listeven[m], lengthofcombs))
    return dict(dic)