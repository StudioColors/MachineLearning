print('Enter a,b and c')

a = int(input())
b = int(input())
c = int(input())

D = b**2 - 4*a*c
print('D = ', D)

if D<0:
    print('No real solutions')
elif D==0:
    x = -b/(2*a)
    print('x = ', x)
elif D>0:
    x1 = (-b + D**0.5)/(2*a)
    x2 = (-b - D**0.5)/(2*a)
    print('x1 = ', x1)
    print('x2 = ', x2)




