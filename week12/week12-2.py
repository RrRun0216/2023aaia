a = list(map(int, input().split() ))

#print( sum(a) )

ans = 0
N = a[0]
for i in range(1, N+1):
	ans += a[i]
	
print(ans)