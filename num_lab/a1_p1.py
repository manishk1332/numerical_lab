import math

x = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
f = [14.5, 19.5, 30.5, 53.5, 94.5, 159.5]

h=x[1]-x[0]

dd = []
dd.append(f)
l = len(f)

for i in range(len(x) - 1):
    temp = []
    for j in range(l-1):
        temp.append(dd[i][j+1]-dd[i][j])
    l-=1
    dd.append(temp)

def poly(x, f, dd):
    for i in range(len(dd)):
        print(dd[i][0]/(math.factorial(i)*math.pow(h, i)), end='')
        for j in range(0,i):
            print('(x-'+str(x[j])+')', end='')

        if(i!=(len(dd)-1)):
            print('+', end='')

    print()

def evl(xi, x, f, dd):
    sum = 0.0
    for i in range(len(dd)):
        coeff = dd[i][0]/(math.factorial(i)*math.pow(h, i))
        mul = 1
        for j in range(0,i):
            mul*=(xi-x[j])

        sum+=coeff*mul

    return sum

poly(x,f,dd)
print(evl(4.5, x, f, dd))