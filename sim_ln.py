import math
err_max = 0
op_fix_one = 1<<28

file_in = open("ln_in.dat","w")
file_out = open("ln_out.dat","w")

fix_one = 1<<25
frac_num = 25

inp = 0.001

inp_max = 0
err_sum = 0
loop_num = 0
bin_x = [0,]
while(inp <32):
	loop_num = loop_num + 1
	din = round(inp*fix_one)
	
	hex_idat = (hex(din & 0xffffffff))
	file_in.write(hex_idat[2:] + "\n")
	
	bin_x = list(bin(din))
	bin_x = bin_x[2:]
	bin_x.reverse()
	cnt = 0
	for i in bin_x:
		if(i!=0):
			valid_bits = cnt+1
		cnt=cnt+1

		
	#print(bin_x)
	#print(valid_bits)
	b = valid_bits - frac_num
	if(valid_bits>32):
		print("error")
		print(hex(din))
		print(inp)
	
	ln_in = din << (32-valid_bits)
	x = ln_in >>(32-28)
	
	#print(hex(ln_in))
	#print(hex(x))
	
	y = 0
	d = 1
	i = 0
	
	while(i<24):
		x_new = x + (x>>i)
		y_new = y - round(op_fix_one * math.log(1+1*(2**(-i))))
		if(x_new<op_fix_one):
			d = 1
			y=y_new
			x=x_new
		else:
			d = 0
			x = x
			y = y
			
		
		i=i+1
		
	bln2 = b * round(math.log(2)*op_fix_one)
	
	odat = y+bln2
	hex_odat = (hex(odat & 0xfffffffff));
	file_out.write(hex_odat[2:] + "\n")
	
	res = (y + bln2)/op_fix_one
	
	
	
	
	
	real = (math.log(din/fix_one))
	if(real!=0):
		err = abs((res-real)/real)
		
	if(err > err_max):
		err_max = err
		inp_max = inp
	
	err_sum = err_sum + err;
	inp = inp + 0.001
	
err_mean = err_sum/loop_num
	
print(err_max)
print(err_mean)
print(inp_max)
print(loop_num)

