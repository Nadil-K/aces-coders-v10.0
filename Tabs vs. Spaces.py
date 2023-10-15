# Tabs vs. Spaces

n=int(input())
for i in range(n):
    a,b = input().split()
    
    if len(a)<len(b):
        print('False')
        continue
        
    while len(b)>0:
        if a[0]==b[0]:
            a=a[1:]
            b=b[1:]
        elif (b[0]=='T' and a[0:2]=='SS'):
            a=a[2:]
            b=b[1:]
        else:
            break

    if len(a)==0 and len(b)==0:
        print('True')
    else:
        print('False')
