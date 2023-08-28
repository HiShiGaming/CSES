n, m, tolerance = map(int, input().split())
applicants = list(map(int, input().split()))
apartments = list(map(int, input().split()))

applicants.sort()
apartments.sort()

print(applicants)
print(apartments)

i = 0 
j = 0
ans = 0

while i < n and j < m:
    if abs(applicants[i] - apartments[j]) <= tolerance:
        ans += 1
        i += 1
        j += 1
    elif applicants[i] < apartments[j]:
        i += 1
    else:
        j += 1

print(ans)
