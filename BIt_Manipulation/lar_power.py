def largest_power( N):
    N = N| (N>>1)
    N = N| (N>>2)
    N = N| (N>>4)
    N = N| (N>>8)
    return (N+1)>>1
n = int(input())
print(largest_power(n))
