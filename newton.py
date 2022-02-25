#newton: x = x- (fx/dfx)

#math.sqrt(y)
from math import remainder


y = 24 

x = 1 
loop = 6 
while(loop >0):
    x=x-(x**2-y)/(2.0*x)
    loop = loop-1
print(x)

#1/12
x = 0.08 
loop =6 
while(loop >0):
    x=2*x-y*(x**2)
    loop = loop-1
print(x)


#26bit numerator /5bit denominator
numerator = 0x12eae94c
denominator = 0xc
remainder = 1
x = 1
loop = 12
accu_div = numerator
avg_tmp = 0
rsh = 0
incb = 0
while(loop >0):
    loop = loop - 1
    if(remainder==0):
        remainder=0x20
        accu_div = 0
    else:
        if(denominator < remainder*2):
            rsh=1
        elif(denominator < remainder*4):
            rsh=2
        elif(denominator < remainder*8):
            rsh=3
        elif(denominator < remainder*16):
            rsh=4
        else:
            rsh=5

        remainder = remainder*2**rsh - denominator 
        accu_div = accu_div>>(rsh-1)   
        incb     = accu_div & 0x1
        accu_div = accu_div>>1   

    avg_tmp = avg_tmp + accu_div + incb

    print("accu_div",accu_div)

print("div res", avg_tmp)


