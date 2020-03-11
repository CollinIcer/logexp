import math

file_in = open("fin.dat","w")
file_out = open("fout.dat","w")
#input : x
# x = k*ln2+y
#e^x = 2^k * e^y


op_scale = 28 #30
op_fix_one = 1<<28

fix_one = 1<<25
fix_one_scale = 25


ln2 = round(math.log(2)*op_fix_one)
ln2_inv = round( (1/math.log(2)) * op_fix_one)

inp = -64#-8.833 #0.001
err = 0
err_max = 0
inp_max = 0

err_max_fix = 0
err_fix = 0
inp_max_fix = 0

err_sum = 0
err_mean = 0
loop_num = 0

while(inp < 64):
	loop_num = loop_num + 1
	
	idat_in = round(inp * fix_one);
	hex_idat = (hex(idat_in & 0xffffffff))
	
	file_in.write(hex_idat[2:] + "\n")
	
	k = ((idat_in * ln2_inv)>>(fix_one_scale + op_scale)) #TODO
	inp_frac = (idat_in<<(op_scale-fix_one_scale)) - (k)*ln2
	
	
	if(inp==64):
		print("debug")
		print((idat_in<<(op_scale-fix_one_scale)))
		print(k) 
		
	if(inp_frac < 0):
		print("error")
	
	
	#cal exp(x), x=0~1
	x = 1 * op_fix_one
	y = inp_frac #0~1.56
	d = 1
	i = 0
	
	while(i<24):
		x_new = x + (x>>i)
		y_new = y - round(op_fix_one * math.log(1+1*(2**(-i))))
		
		if(y_new>=0):
			d = 1
			y=y_new
			x=x_new
		else:
			d = 0
			x = x
			y = y

		i=i+1
	
	#print(x/fix_one)
	#print(math.exp(inp_frac/fix_one))
	
	hex_odat = (hex(x & 0xffffffff));
	hex_k    = (hex(k & 0xff))
	file_out.write(hex_odat[2:] + "\n")
	file_out.write(hex_k[2:] + "\n")
	
	res = x/op_fix_one * (2**(k))

	
	real = math.exp(inp)
	err = abs((real-res)/real)
		
	if(err_max < err):
		err_max = err
		inp_max = inp
		
	err_sum = err_sum + err

	inp = inp + 0.001
		

err_mean = err_sum/loop_num
print(err_max)
print(err_mean)
print(inp_max)
print(loop_num)



