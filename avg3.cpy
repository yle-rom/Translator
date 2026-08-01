#int result
def avg3(x,y,z) :
#{
	global result
	result = (x+y+z)//3
	return result
#}

#def main 
#int i
i= 0
while i != 10 :
#{
	if i == 2 :
		print(avg3(5,5,5))
	elif i == 4 :
		print(avg3(4,6,5))
	else :
		print(avg3(i,3,5))
	i = i + 1
#}
	