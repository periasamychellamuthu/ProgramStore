#find maximum number of queens to be plaed in a given square.

def NQueens(length,square,column,count):
	if(column<length):
		for row in range(length):
			if(checkQueenPossible(column,row,square)):
				square[row][column]=1
				print("queen place succeeded")
				childPossibilitesCount = NQueens(length,square,column+1,count)
				print("child possibilities count for columns {} and row {} and count is {}".format(row,column,childPossibilitesCount))
				if(childPossibilitesCount+1 > count):
					count = childPossibilitesCount+1
				square[column][row]=0
		return count
	else:
		return 0

def checkQueenPossible(column,row,square):
	size = len(square)
	return horizontalCheck(column,row,square,size) and verticalCheck(column,row,square,size) and crossCheck(column,row,square,size)


def horizontalCheck(column,row,square,size):
	print("horizontalCheck entered {},{}  and size {} and square is {}".format(row,column,size,square))
	for i in range(size):
		if(i!=column and square[row][i]==1):
			return False
	print("horizontalCheck exit with True")
	return True

def verticalCheck(column,row,square,size):
	print("verticalCheck entered")
	for i in range(size):
		if(i!=row and square[i][column]==1):
			return False
	print("verticalCheck exit with True")		
	return True

def crossCheck(column,row,square,size):
	return crossUp(column,row,square,size) and crossDown(column,row,square,size)


def crossUp(column,row,square,size):
	print("crossUp entered")
	XPos,YPos=row,column
	# left cross Up
	while(XPos>=0 and YPos>=0 and XPos<size and YPos<size):
		if(square[XPos][YPos]==1):
			return False
		XPos=XPos-1
		YPos=YPos-1
	XPos,YPos=row,column
	# right cross Up
	while(XPos>=0 and YPos>=0 and XPos<size and YPos<size):
		if(square[XPos][YPos]==1):
			return False
		XPos=XPos-1
		YPos=YPos+1
	print("crossUp exit with True")
	return True

def crossDown(column,row,square,size):
	print("crossDown entered")
	XPos,YPos=row,column
	# left cross Down
	while(XPos>=0 and YPos>=0 and XPos<size and YPos<size):
		if(square[XPos][YPos]==1):
			return False
		XPos=XPos+1
		YPos=YPos-1
	XPos,YPos=row,column
	# right cross Down
	while(XPos>=0 and YPos>=0 and XPos<size and YPos<size):
		if(square[XPos][YPos]==1):
			return False
		XPos=XPos+1
		YPos=YPos+1
	print("crossDown exit with True")
	print("cross down check succeed for row {} , column {}".format(row,column)) 
	return True


if __name__ == '__main__':
	length = 3
	print(NQueens(length,[[0]*length for _ in range(length)],0,0))