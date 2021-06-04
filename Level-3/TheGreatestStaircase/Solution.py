def solution(numbricks):
    hi = 1
    global cache
    cache = [[None]*(numbricks+2) for i in range(numbricks+1)]
    return getnum2(numbricks,hi)-1
def getnum2(num,hi):
    if cache[num][hi]!=None:
        return cache[num][hi]
    if num==0:
        return 1
    elif num<hi:
        return 0
    else:
        cachenum=getnum2(num-hi,hi+1)+getnum2(num,hi+1)
        cache[num][hi] = cachenum
        return cachenum
print(solution(800))
