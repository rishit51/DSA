n = int(input())
arr = list(map(int, input().split()))

p1 = [0]*n
p1[0] = max(0, arr[0])
for i in range(1, n):
    p1[i] = max(0, arr[i], p1[i-1] + arr[i])

p2 = [0]*n
p2[-1] = max(0, arr[-1])
for i in range(n-2, -1, -1):
    p2[i] = max(0, arr[i], p2[i+1] + arr[i])

bestLeft = [0]*n
bestLeft[0] = p1[0]
for i in range(1, n):
    bestLeft[i] = max(bestLeft[i-1], p1[i])


bestRight = [0]*n
bestRight[-1] = p2[-1]
for i in range(n-2, -1, -1):
    bestRight[i] = max(bestRight[i+1], p2[i])

ans = 0
for i in range(n-1):
    ans = max(ans, bestLeft[i] + bestRight[i+1])

print(ans)



