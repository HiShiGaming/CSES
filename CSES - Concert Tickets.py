n,m = map(int, input().split())
h = list(reversed(sorted(list(map(int, input().split())))))
t = list(map(int, input().split()))
n = list(reversed(sorted(map(int,t))))
ans = [-1]*len(t)
i = 0
j = 0
while i < len(t) and j < len(h) :
    if n[i] - h[j] >= 0:
        ans[t.index(n[i])] = h[j]
        i += 1
        j += 1
    elif n[i] < h[j]:
        j += 1
    elif n[i] > h[j]:
        i += 1
    else :
        ans[t.index(t[i])] = -1
for s in ans:
    print(s)
    
