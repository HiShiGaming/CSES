def check(z):
    z=str(i)
    n=[i for i in z]
    re="".join(n[::-1])
    if z==re:
        return True
    else:return False
l,r=list(map(int,input().split()))
ans=0
for i in range(l,r+1):
    if check(i):
        ans+=1
print(ans)
    
