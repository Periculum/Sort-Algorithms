#!/usr/bin/env python3

import random

def bogosort(a): 
  while True: 
    random.shuffle(a) 
    if check_if_sorted(a): 
      return a

def check_if_sorted(a):
    for n in range(len(a) - 1):
      if a[n] > a[n + 1]:
        return False
    return True               

def main():
    a = [4, 2, 5, 0, 7, 11]
    print(bogosort(a))

if __name__ == '__main__':
    main()