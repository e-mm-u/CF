x = int(input())

for i in range(0,x):
    f = int(input())
    s = input()
    q = []
    for i in range(f):
        if(s[i] == 'Q'):
            q.append(s[i])
        elif(s[i]=='A' and len(q)!=0):
            q.pop()
            
    if(len(q) == 0):
        print('Yes')
    else:
        print('No')
    