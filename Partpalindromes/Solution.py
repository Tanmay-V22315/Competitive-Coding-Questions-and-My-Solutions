def solution(inpstring):
    inpstring = inpstring.lower()
    inpstring = inpstring.replace(" ",'')
    print(inpstring)
    letlist = list(inpstring)
    finlist = []
    palinset = []
    for i in range(0,len(inpstring)+1):
        for j in range(0,len(inpstring)+1):
            if inpstring[i:i+j]!='':
                finlist.append(inpstring[i:i+j])
    finlist.sort()
    for i in finlist:
        if list(i)==list(reversed(i)):
            palinset.append(i)
    palinset.sort()
    print(list(set(palinset)))
solution(input("Word: "))
