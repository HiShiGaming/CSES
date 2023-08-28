def logic(d,m,y,k):
    d1,m1,y1=0,0,0
    thang30=[4,6,9,11]
    thang31=[1,3,5,7,8,10,12]
    if m in thang30:
        d1=d+k
        m1=round(d1/30)
        y1=y+m1
    if m in thang31:
        d1=d+k
        m1=round(d1/31)
        y1=y+m1
    for i in range(y,y1+1):
        if i%4==0:
            
n=int(input())
for i in range(n):
    d,m,y,k=list(map(int,input().split()))
    
