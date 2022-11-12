x = int(input())

for i in range(0,x):
    f = int(input())
    s = input()
    Q = 0
    for i in range(f):
        if(s[i] == 'Q'):
            Q = Q + 1
        elif(s[i]=='A' and Q>0):
            Q = Q - 1
            
    if(Q == 0):
        print('Yes')
    else:
        print('No')