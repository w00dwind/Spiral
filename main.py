n = 5

a = [[0 for j in range(n)] for i in range(n) ]
i,j = 0,0
for v in range(1,n**2+1):
    a[i][j] = v
    if v == n**2: break
    if i<=j+1 and i+j<n-1: j+=1  # Проверяем, если номер строки меньше или равен номеру столбца и строка+столбец < n-1
    elif i<j and i+j>=n-1: i+=1
    elif i>=j and i+j>n-1: j-=1
    elif i>j+1 and i+j<=n-1: i-=1

for i in range(n):
    print(*a[i])






