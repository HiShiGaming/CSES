n=input()
s=set([i for i in n])
res,cnt=0,1
for i in range(1,len(n)):
    if n[i]==n[i-1]:
        cnt+=1
    else:
        cnt=1
    res=max(res,cnt)
print(res)
