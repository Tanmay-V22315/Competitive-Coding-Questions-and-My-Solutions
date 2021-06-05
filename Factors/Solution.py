def finfactors(numinp):
    factlist = []
    upnum = str(1)+str(0)*(len(str(numinp))-1)
    for i in range(1,int(upnum)):
        if numinp%i==0:
            factlist.append(i)
    finlist = []+factlist
    for j in factlist:
        testnum = (numinp/j)
        finlist.append(testnum)
    finlist = list(set(finlist))
    finlist.sort()
    print finlist
