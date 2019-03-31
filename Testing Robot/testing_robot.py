for _t in range(int(input())):
    N, S = map(int,input().split())
    steps = input()
    #print(N,S,steps)
    pos = [S]
    cnt = 1
    for x in steps:
        if(x == 'R'):
            step = 1
        else:
            step = -1
        
        S += step

        if S not in pos:
            pos.append(S)
            cnt += 1
    print(cnt)