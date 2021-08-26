# https://www.hackerrank.com/challenges/making-candies/problem?h_r=internal-search


import sys
def candies(arr):
	total,leftRight,rightLeft=0,[1]*len(arr),[1]*len(arr)
	# left to right traversal
	for i in range(1,len(arr)):
		if(arr[i] > arr[i-1]):
			leftRight[i]=leftRight[i-1]+1
	for i in range(len(arr)-2,-1,-1):
		if(arr[i] > arr[i+1]):
			rightLeft[i]=rightLeft[i+1]+1
	for i in range(len(arr)):
		total+=max(leftRight[i],rightLeft[i])
	print(total)

def makingCandies(m,w,p,n,retainedCandies,passes,step):
	retainedCandies+=m*w
	if retainedCandies>=n or (m*w)>=n:
		if passes==0 or passes>step:
			passes=step
		return passes
	passes = makingCandies(m,w,p,n,retainedCandies,passes,step+1)
	if(retainedCandies/p>0):
		passes = makingCandies(m+(retainedCandies/p),w,p,n,retainedCandies%p,passes,step+1)
		passes = makingCandies(m,w+(retainedCandies/p),p,n,retainedCandies%p,passes,step+1)
	return passes


def minimumPasses(m, w, p, n):
	print(makingCandies(m,w,p,n,0,0,1))


if __name__=="__main__":
	# candies([1,2,2,1])
	minimumPasses(1,1,6,45)
	# minimumPasses(3,1,2,12)
	# minimumPasses(5184889632,5184889632,20,10000)



