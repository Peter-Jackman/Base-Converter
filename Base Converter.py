def d2x(n,x):
    num=[]
    ans=0
    for y in str(n):
        num.append(int(y))
    
    for y in range(len(num)):
        ans+=num[y]*(x**(len(num)-y-1))

    return ans

n=int(input('What number do you want to convert?'))
x=int(input('What base is that number?'))
print(d2x(520,100))
