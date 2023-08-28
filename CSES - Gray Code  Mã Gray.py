def natural_to_gray(n: int) -> int:
    return n ^ (n >> 1)
def natural_to_binary(n: int) -> str:
    return bin(n)[2:]
def natural_to_gray2bit(n: int) -> str:
    gray = n ^ (n >> 1)
    return format(gray, '02b')
n=int(input())
for i in range(0,2**n):
    print(natural_to_gray2bit(i))

    
