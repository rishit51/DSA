def maximum(a, b, c):
    n = len(a)

    dp = [[0]*3 for _ in range(n)]
    ls=[a,b,c]

    
    for j in range(3):
        dp[0][j]=ls[j][0]

    for i in range(1, n):
        for j in range(3):
            possi =[]
            for pos in range(3):
                if pos!=j:
                    possi.append(dp[i-1][pos]+ls[j][i])
            dp[i][j]=max(possi)

    return max(dp[-1])