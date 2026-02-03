def getTime(intervals: list[str], k):
    ans = [0]*(60*25)
    n = 23*60 + 59   # 1439

    for activity in intervals:
        person , action , start , end = activity.split()

        sh = int(start[:2])
        sm = int(start[2:])
        eh = int(end[:2])
        em = int(end[2:])

        s = sm + 60*sh
        e = em + 60*eh

        ans[s] += 1
        ans[e+1] -= 1

   
    for i in range(1, n+1):
        ans[i] += ans[i-1]

  
    bad = 0

    
    for i in range(k):
        if ans[i] != 0:
            bad += 1

    if bad == 0:
        return 0, k-1

    l = 0
    for r in range(k, n+1):
        if ans[r] != 0:
            bad += 1
        if ans[l] != 0:
            bad -= 1
        l += 1

        if bad == 0:
            hh = l // 60
            mm = l % 60
            return f"{hh:02d}{mm:02d}"

    return -1

        
        
        
        