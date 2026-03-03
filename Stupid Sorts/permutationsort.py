#!/usr/bin/env python3

from itertools import permutations

def permutationsort(a):
    p = list(permutations(a))
    for perm in p:
        for n in range(len(a) - 1):
            if check_if_sorted(perm):
                return perm

def check_if_sorted(a):
    for n in range(len(a) - 1):
      if a[n] > a[n + 1]:
        return False
    return True               

def main():
    a = [4, 2, 5, 0, 7, 11]
    print(permutationsort(a))

if __name__ == '__main__':
    main()