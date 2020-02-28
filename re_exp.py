import math
err_max = 0
inp = 0.001
fix_one = 1<<24

while(inp <1.0):
	x = 1 * fix_one
	y = inp * fix_one #0~1.56
	d = 1
	i = 0
	#while((abs(y))>0.0001):
	while(i<24):
		x_new = x + (x>>i)
		y_new = y - round(fix_one * math.log(1+1*(2**(-i))))
		if(y_new>=0):
			d = 1
			y=y_new
			x=x_new
		else:
			d = 0
			x = x
			y = y
			
		
		i=i+1
		
	res = x/fix_one
	real = math.exp(inp)
	err = abs((res-real)/real)
	if(err > err_max):
		err_max = err
	
	inp = inp + 0.001
	
print(err_max)



#while(inp <1.0):
#	x = 1
#	y = inp #0~1.56
#	d = 1
#	i = 0
#	#while((abs(y))>0.0001):
#	while(i<24):
#		x_new = x*(1+1*(2**(-i)))
#		y_new = y - math.log(1+1*(2**(-i)))
#		if(y_new>=0):
#			d = 1
#			y=y_new
#			x=x_new
#		else:
#			d = 0
#			x = x
#			y = y
#			
#		
#		i=i+1
#		
#	res = x
#	real = math.exp(inp)
#	err = (abs(res-real))/real
#	if(err > err_max):
#		err_max = err
#	
#	inp = inp + 0.001
	
#print(err_max)
