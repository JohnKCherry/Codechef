t = int(input())

def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

for _ in range(t):
    N, A, B, K = map(int, input().split())
 
    lcm = lcm(A,B)

    a = N/A - N/lcm
    b = N/B - N/lcm

    if(a+b < K):
        print('Lose')
    else:
        print('Win')
    