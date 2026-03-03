#!/usr/bin/env python3

import threading
import time

def sleepsort(a): 
    result = [] 
    threads = [threading.Thread(target=sleeper, args=(n, result) ) for n in a] 
    [t.start() for t in threads]
    [t.join() for t in threads]
    return result
 
def sleeper(n, result):
    time.sleep(n)
    result.append(n)

def main():
    a = [4, 2, 5, 0, 7]
    print(sleepsort(a))

if __name__ == '__main__':
    main()