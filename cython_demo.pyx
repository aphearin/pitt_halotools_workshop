#!/usr/bin/env python

def nth_prime_cython(int nth_prime):
    cdef int n, k, i, result

    cdef int p[10000]

    k = 0
    n = 2

    while k < nth_prime:
        i = 0
        while i < k and n % p[i] != 0:
            i = i + 1
        if i == k:
            p[k] = n
            k = k + 1
            result = n
        n = n + 1

    return result