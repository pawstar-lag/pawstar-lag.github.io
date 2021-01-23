#!/usr/bin/env python3
def mean(v):
	sum=0
	a=len(v)
	for i in v:
		sum+=i
	return(sum/a)
if __name__=='__main__':
	v=[60,29,799999999]
	print(mean(v))
