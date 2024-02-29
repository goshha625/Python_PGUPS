x=int(input())
a=(x//1000)
b=(x//100-x//1000*10)
c=x//10-x//100*10
d=x%10
if b==c==d==0:
    print(x)
else:
    if b==c==0:
        m1=min(a, d)
    elif b==d==0:
        m1=min(a, c)
    elif c==d==0:
        m1=min(a, b)
    elif b==0:
        m1=min(a, d, c)
    elif c==0:
        m1=min(a, d, b)
    elif d==0:
        m1=min(a, b, c)
    else:
        m1=min(a, b, c, d)
    if a==m1:
        m2=min(b, c, d)
    elif (b==m1):
        m2=min(a, c, d)
    elif (c==m1):
        m2=min(a, b, d)
    else:
        m2=min(a, b, c)
    m4=max(a, b, c, d)
    m3=a+b+c+d-m1-m2-m4
    print(m1, m2, m3, m4, sep="")