t = int(input())
for _ in range(t):
    y, x = map(int, input().split())
    if y > x:
        if y % 2 == 1:
            print(y**2 - x + 1)
        else:
            print((y-1)**2 + x)
    else:
        if x % 2 == 0:
            print(x**2 - y + 1)
        else:
            print((x-1)**2 + y)
