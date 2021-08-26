# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem?h_r=profile

# use quick sort to sort element in array
def sort(arr,start,end):
	if(start<end):
		pos,pivot= -1,arr[end]
		for i in range(start,end):
			if arr[i]>pivot and pos==-1:
				pos=i
			elif pivot>=arr[i] and pos!=-1:
				temp = arr[pos]
				arr[pos] = arr[i]
				arr[i] = temp
				pos+=1
		if pos==-1:
			pos=start
		if arr[pos]>pivot:
			temp=arr[pos]
			arr[pos]=arr[end]
			arr[end]=temp
		else:
			pos=end
		sort(arr,start,pos-1)
		sort(arr,pos+1,end)

# use binary search to search element in array
def binarySearch(arr,amount,start,end):
	if start<=end:
		middleElementPos = (start+end)/2
		if arr[middleElementPos]>amount:
			return binarySearch(arr,amount,start,middleElementPos-1)
		elif arr[middleElementPos]<amount:
			return binarySearch(arr,amount,middleElementPos+1,end)
		elif arr[middleElementPos]==amount:
			return middleElementPos
	else:
		return 0

# actual logic of problem
def getFlavour(temp,amount):
	flavour1,flavour2,arr = 0,0,temp[:]
	sort(arr,0,len(arr)-1)
	i = binarySearch(arr,amount/2,0,len(arr))
	if len(temp)>=i+1 and arr[i]== arr[i+1]:
		i+=1
	print(i,amount/2)
	left,right,flag=(i-1),i,True
	while flag:
		if (arr[right]+arr[left])>amount:
			left-=1
		elif (arr[right]+arr[left])<amount:
			right+=1
		else:
			flag = False
	flavour1=temp.index(arr[left])
	flavour2 = temp.index(arr[right])
	if flavour1==flavour2:
		flavour2 = temp.index(arr[right],1)
	print(flavour1+1,flavour2+1)

if __name__=="__main__":
	array= [5,3,2,4,6,2,1,7]
	# array= [2,2,4,3]
	getFlavour(array,5)
	print(array)
