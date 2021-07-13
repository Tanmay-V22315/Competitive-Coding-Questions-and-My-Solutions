def solution(start, length):
    allnum = range(start,start+length**2)
    divnum = []
    for i in range(0,len(allnum),length):
        divnum.append(allnum[i:i+length])
    for i in divnum:
        del i[length-divnum.index(i):length]
    finnum = []
    for i in divnum:
        finnum += i
    counter = 1
    initbin = finnum[0]
    while counter!=len(finnum):
        initbin = initbin^finnum[counter]
        counter += 1
    return(initbin)
