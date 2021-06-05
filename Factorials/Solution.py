def solution(intinp):
    global memo
    memo = [None]*(intinp+1)
    return getfact(intinp)
def getfact(numinp):
    if numinp==0:
        return 1
    elif numinp==1:
        return 1
    elif memo[numinp]!=None:
        return memo[numinp]
    else:
        outsol = numinp*getfact(numinp-1)
        memo[numinp-2]=outsol
        return outsol

