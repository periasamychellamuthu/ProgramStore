# https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
import sys;

class kadaneAlgo:
    def __init__(self):
        self.sum=0
        self.max=-sys.maxsize-1

    def proc(self,array):
        for i in range(len(array)):
            self.sum = self.sum+array[i]
            if self.sum>self.max:
                self.max=self.sum
            elif self.sum<0:
                self.sum=0
        return self.max


# if __name__=="__main__":
#     length = int(input("enter the length"))
#     li = list()
#     for _ in range(length):
#         li.append(int(input()))
#     print('result : ',kadaneAlgo().proc(li))
