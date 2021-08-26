
# https://www.hackerrank.com/challenges/road-maintenance/problem

import math
import os
import random
import re
import sys

def tollCostDigits(road_from,road_to,road_weight,pos,source,destination,result,cost):
	
	for i in range(len(road_from)):
		if pos != i:
			if ((road_to[i] != source) and (destination == road_from[i]) or source==0):
				result[(cost+road_weight[i])%10]+=1
				tollCostDigits(road_from,road_to,road_weight,i,(road_from[i] if (source==0) else source),road_to[i],result,cost+road_weight[i])
			if ((road_from[i] != source) and (destination == road_to[i]) or source==0):
				result[(cost+(1000-road_weight[i]))%10]+=1
				tollCostDigits(road_from,road_to,road_weight,i,(road_to[i] if (source==0) else source),road_from[i],result,cost+(1000-road_weight[i]))	
	return result

if __name__ == '__main__':
    road_nodes, road_edges = 3,3

    road_from = [1,1,2]
    road_to = [3,2,3]
    road_weight = [602,256,411]

    # for i in range(road_edges):
    #     road_from[i], road_to[i], road_weight[i] = map(int, input().split())

    for i in tollCostDigits(road_from,road_to,road_weight,sys.maxsize,0,1,[0]*10,0):
    	print i











