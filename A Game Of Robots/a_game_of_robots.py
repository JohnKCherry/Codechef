t  = int(input())

for _ in range(t):
    string = [s for s in input()]
    
    flag = True
    idx = 0
    while(idx<len(string)):

        if( string[idx] != '.'):
            digits = int(string[idx])
            for i in range(1,digits+1):
                if(idx-i >= 0 ):
                    if(string[idx-i] == '.'): string[idx-i] = string[idx]
                    else:
                        flag = False
                        break
                if(idx+i < len(string) ):
                    if(string[idx+i] == '.'): string[idx+i] = string[idx]
                    else:
                        flag = False
                        break
            idx += digits+1
        else:
            idx += 1
            
        
    
    if flag:
        print('safe')
    else:
        print('unsafe')
