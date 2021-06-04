def solution(inpstring):
    inpstring = inpstring.lower().replace(" ",'')
    letlist = list(inpstring)
    finlist = []
    palinset = []
    for i in range(0,len(inpstring)+1):      #Generate all possible substrings of given string
        for j in range(0,len(inpstring)+1):  
            if inpstring[i:i+j]!='':
                finlist.append(inpstring[i:i+j])
    finlist.sort()
    for i in finlist: #Check palindromes
        if list(i)==list(reversed(i)):
            palinset.append(i)
    palinset.sort() #Not particularly important
    return(list(set(palinset)))

