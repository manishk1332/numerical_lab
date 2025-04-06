x = [0,2,4,6]
f = [1,-1,3,4]

def poly(x,f):
    for i in range(len(x)):
        mul = 1
        for j in range(len(x)):
            if(j==i): continue
            mul*=(x[i]-x[j])

        coeff = f[i]/mul
        print(coeff, end='')

        for j in range(len(x)):
            if(j==i): continue
            print('(x-'+str(x[j])+')', end='')
        if(i!=(len(x)-1)) : print('+', end='')
    print()

def evl(xi,x,f):
    sum = 0
    for i in range(len(x)):
        mul = 1
        for j in range(len(x)):
            if(j==i): continue
            mul*=(x[i]-x[j])

        coeff = f[i]/mul

        mul = 1
        for j in range(len(x)):
            if(j==i): continue
            mul*=(xi-x[j])
        sum+=(coeff*mul)
    
    return sum

poly(x,f)
print(evl(3.5,x,f))