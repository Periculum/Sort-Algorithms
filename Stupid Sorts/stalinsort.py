#!/usr/bin/env python3

def stalinsort(a):
	result = []
	max = a[0]
	for n in range(len(a)):
		if a[n] >= max:
			result.append(a[n])
			max = a[n]
	return result              

def main():
    a = [4, 2, 5, 0, 7, 11]
    print(stalinsort(a))

if __name__ == '__main__':
    main()
