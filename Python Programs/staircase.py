# https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem?h_r=profile

# method 1
def staircase(length,total,count):
	for i in range(1,4):
		if (total+i)<length:
			count=staircase(length,total+i,count)
		elif (total+i)==length:
			print(arr,total)
			count+=1
		elif (total+i)>length:
			break
	return count

# method 2
def staircase2(length):
	if length==0:
		return 1
	elif length<0:
		return 0
	elif length>0:
		return staircase2(length-1)+staircase2(length-2)+staircase2(length-3)

# method 3 stable and efficient
def staircase3(n):
    st1, st2, st3 = 1, 2, 4
    
    for _ in range(n-1):
        st1, st2, st3 = st2, st3, st1 + st2 + st3

    return st1


if __name__=="__main__":
	print(staircase3(5))