n=int(input())
arr=[int(i) for i in range(1,n+1)]
ans=[]
if n==1 or n==0:
    print("NO SOLUTION")
else:
    for i in range(1,n+1,2):
        ans.append(i)
        arr.remove(i)
    if abs(ans[len(ans)-1]-arr[0])==1:
        print("NO SOLUTION")
    else:
        ans.extend(arr)
        print(" ".join(map(str,ans[::-1])))

