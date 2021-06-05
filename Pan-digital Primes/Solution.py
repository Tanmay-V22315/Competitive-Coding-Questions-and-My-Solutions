def solution(inpnum):
    upnum = int(str(9)*inpnum)
    lownum = int(str(1)+(str(0)*(inpnum-1)))
    ansnum = None
    for i in range(upnum,lownum,-1):
        if len(str(i))==len(set(str(i))):
            if 2**(i-1)%i==1:
                ansnum = i
                break
    return ansnum

