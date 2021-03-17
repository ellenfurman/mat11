
def XtimesY(x,y):
    if x<=0:
        return 0
    number=exponent(y*ln(x))
    return(number)

def exponent(x):
    i=1
    j=1
    assembly=1
    e_x=1
    x_n=1
    while i<150: 
        assembly=i*j
        j=assembly
        i=i+1
        x_n=x_n*x
        e_x=e_x+x_n/assembly  
    return(e_x)

def ln(x):
    y=0
    y_n1=0
    while y<1000:
        y_n1=y_n1+2*((x-exponent(y_n1))/(x+exponent(y_n1)))
        y=y+1
    return(y_n1)

def sqrt(x,y):
    outcome=XtimesY(y, 1/x)
    return(outcome)

def calculate(x):
    calc=exponent(x)*XtimesY(7,x)*XtimesY(x, -1)*sqrt(x,x)
    return(calc)
    
x=float(input())
print(calculate(x))
    
