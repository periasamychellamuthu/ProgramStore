def positionCheck(x,y,element,resultGrid):
	left = x-1
	right = x+1
	top = y-1
	botton = y+1


def elementCheck(x,y,element,resultGrid,opt):
	if resultGrid[x][y]==[]:
		return true
	else:
		validateElement(opt,element,resultGrid[x][y]);


def validateElement(opt,element,gridElement):
	if opt is "Left":
		return element[3]==gridElement[1]
	else if opt is "Right":
		return element[1]==gridElement[3]
	else if opt is "Top":
		return element[0]==gridElement[2]
	else if opt is  "Bottom":
		return element[2]==gridElement[0]
