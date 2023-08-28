n,x = list(map(int,input().split()))
a = sorted(list(map(int,input().split())))
cnt = 0
check = 0
i = 0
j = n - 1
while i <= j :
    check = a[i] + a[j]
    if check <= x :
        i += 1
    j -= 1
    cnt += 1
print(cnt)
