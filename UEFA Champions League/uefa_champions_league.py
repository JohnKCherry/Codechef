for _i in range(int(input())):
    line = []
    for i in range(12):
        line.append(input())

    points = {}
    goals = {}

    for l in line:
        teamA, goalA, _, goalB, teamB = l.split()
        
        if teamA not in points.keys():
            points[teamA] = 0
            goals[teamA] = 0
        if teamB not in points.keys():
            points[teamB] = 0
            goals[teamB] = 0
        
        df = int(goalA) - int(goalB)

        if(df == 0):
            points[teamA] += 1
            points[teamB] += 1
        elif(df > 0):
            points[teamA] += 3
        else:
            points[teamB] += 3
        
        goals[teamA] += df
        goals[teamB] -= df
    
    f = []

    for k in points.keys():
        f.append((k,points[k],goals[k]))
        
    f.sort(key=lambda x:x[2], reverse=True)
    f.sort(key=lambda x:x[1], reverse=True)

    print(f[0][0], f[1][0])