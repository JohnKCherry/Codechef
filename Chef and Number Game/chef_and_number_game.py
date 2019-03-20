from math import pow

t = int(input())

for _ in range(t):
    N = int(input())
    A = map(int,input().split())

    pos = 0 
    neg = 0
    for s in A:
        if s>=0:
            pos +=1
        else:
            neg +=1
    if(pos == N or neg == N):
        print(N,N,sep=' ')
    else:
        print(max(pos,neg), min(pos,neg), sep=' ')