

t = int(input())

for _ in range(t):
    N = int(input())
    A = map(int, input().split())
    D = map(int, input().split())

    ans = -1
    for i in range(N):
        if(A[i-1]+A[(i+1)%n] < B[i]):
            ans = max(ans,B[i])
    print(ans)