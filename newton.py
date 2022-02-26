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

#1/y
x = 0.08 
loop =6 
while(loop >0):
    x=2*x-y*(x**2)
    loop = loop-1
print(x)


#26bit numerator /5bit denominator
numerator = 0x140fe386
denominator =12
remainder = 1
x = 1
loop = 12
accu_div = numerator
avg_tmp = 0
rsh = 0
incb = 0
#while(loop >0):
while(accu_div>0):
    loop = loop - 1
    if(remainder==0):
        remainder=0x20
        accu_div = 0
    else:
        if(denominator <= remainder*2):
            rsh=1
        elif(denominator <= remainder*4):
            rsh=2
        elif(denominator <= remainder*8):
            rsh=3
        elif(denominator <= remainder*16):
            rsh=4
        else:
            rsh=5
        #print("rsh",rsh)
        remainder = remainder*2**rsh - denominator 
        #print("remainder:",remainder)
        accu_div = accu_div>>(rsh-1)   
        incb     = accu_div & 0x1
        accu_div = accu_div>>1   
        print("accu_div",accu_div)

    avg_tmp = avg_tmp + accu_div + incb

    #print("accu_div",accu_div)

print("div res", avg_tmp)


A=numerator
B=denominator
FN=0
C=0
i=32+FN
B=B*(2**32)*(2**FN)
A=A*2**FN
while(i>=0):
    if(A>B):
        C=C+2**i
        A=A-B
    B=B>>1
    i=i-1
    
print(C)
print(A)


#module div #(
#    parameter WIDTH=4,  // width of numbers in bits
#    parameter FBITS=0   // fractional bits (for fixed point)
#    ) (
#    input wire logic clk,
#    input wire logic start,          // start signal
#    output     logic busy,           // calculation in progress
#    output     logic valid,          // quotient and remainder are valid
#    output     logic dbz,            // divide by zero flag
#    output     logic ovf,            // overflow flag (fixed-point)
#    input wire logic [WIDTH-1:0] x,  // dividend
#    input wire logic [WIDTH-1:0] y,  // divisor
#    output     logic [WIDTH-1:0] q,  // quotient
#    output     logic [WIDTH-1:0] r   // remainder
#    );
#
#    // avoid negative vector width when fractional bits are not used
#    localparam FBITSW = (FBITS) ? FBITS : 1;
#
#    logic [WIDTH-1:0] y1;           // copy of divisor
#    logic [WIDTH-1:0] q1, q1_next;  // intermediate quotient
#    logic [WIDTH:0] ac, ac_next;    // accumulator (1 bit wider)
#
#    localparam ITER = WIDTH+FBITS;  // iterations are dividend width + fractional bits
#    logic [$clog2(ITER)-1:0] i;     // iteration counter
#
#    always_comb begin
#        if (ac >= {1'b0,y1}) begin
#            ac_next = ac - y1;
#            {ac_next, q1_next} = {ac_next[WIDTH-1:0], q1, 1'b1};
#        end else begin
#            {ac_next, q1_next} = {ac, q1} << 1;
#        end
#    end
#
#    always_ff @(posedge clk) begin
#        if (start) begin
#            valid <= 0;
#            ovf <= 0;
#            i <= 0;
#            if (y == 0) begin  // catch divide by zero
#                busy <= 0;
#                dbz <= 1;
#            end else begin
#                busy <= 1;
#                dbz <= 0;
#                y1 <= y;
#                {ac, q1} <= {{WIDTH{1'b0}}, x, 1'b0};
#            end
#        end else if (busy) begin
#            if (i == ITER-1) begin  // done
#                busy <= 0;
#                valid <= 1;
#                q <= q1_next;
#                r <= ac_next[WIDTH:1];  // undo final shift
#            end else if (i == WIDTH-1 && q1_next[WIDTH-1:WIDTH-FBITSW]) begin // overflow?
#                busy <= 0;
#                ovf <= 1;
#                q <= 0;
#                r <= 0;
#            end else begin  // next iteration
#                i <= i + 1;
#                ac <= ac_next;
#                q1 <= q1_next;
#            end
#        end
#    end
#endmodule
