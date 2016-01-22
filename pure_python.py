#!/usr/bin/env python

def nth_prime_pure_python(nth_prime):

    k = 0
    n = 2
    p = []

    while k < nth_prime:
        i = 0
        while i < k and n % p[i] != 0:
            i = i + 1
        if i == k:
            p.append(n)
            k = k + 1
            result = n
        n = n + 1

    return result