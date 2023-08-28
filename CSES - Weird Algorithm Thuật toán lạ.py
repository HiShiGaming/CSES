n=int(input())
ans=[n]
while n!=1:
    if n%2==0:
        n//=2
        ans.append(n)
    else:
        n=(n*3)+1
        ans.append(n)
print(" ".join(map(str,ans)))


        
        
