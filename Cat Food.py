# Cat Food

n = int(input())
for i in range(n):
    print(' '*(n+1) + ' ' * (n-i-1) + '*' * (3*i+1) + ' '*2*n + ' ' * 4 *(n-i-1) + '*' * (3*i+1))
for i in range(n//2):
    print(' '*(n+1) + '*' * 2* (n +(3*n-2)))
for i in range(n-(n//2)):
    print(' '*(n+1) + '*' * n + ' ' * n + '*'*4*(n-1) + ' ' * n + '*' * n)

for i in range(n//2):
    print(' '*i + ('*'*n + ' ')*((i+1)%2) + ' '*(n+1)*(i%2) + '*' * (3*n-2) + ' ' * 2*(n-i) + '*' * (3*n-2)+ (' '+'*'*n)*((i+1)%2))
    
for a in range(i+1,n):
    print(' ' * a + ('*'*n + ' ')*((a+1)%2) + ' '*(n+1)*(a%2) + '*'*(((n*5+(n-2))//2)-2+(n-a)) + '  ' + '*'*(((n*5+(n-2))//2)-2+(n-a))+ (' '+'*'*n)*((a+1)%2))
    
for i in range(n):
    print(' '*(n+1) + ' '*(n-1-i) + '*' * (n*5+(n-2)+2*i))