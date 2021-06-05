
oddcompnumlist = []
for i in range(2,10000):
    if i%2!=0:
        if 2**(i-1)%i!=1:
            oddcompnumlist.append(i)
primlist = []
randlist = []
complist = []
for j in range(2,142):
    boolist = []
    for k in range(2,j):
        if j%k != 0:
            boolist.append('false')
        elif j%k == 0:
            boolist.append('true')
            break
    if 'true' in boolist:
        randlist.append(j)
    else:
        primlist.append(j)
        randlist.append(j)
for m in primlist:
    complist.extend(range(2*m,10000,m))
    complist.append(m**2)
complist = list(set(complist))
complist.sort()
primrange = range(2,10000)
for s in complist:
    try:
        primrange.remove(s)
    except:
        pass
squareslist = []
for i in range(1,600):
    squareslist.append(2*(i**2))
goldbacknl = []
for w in primrange:
    for a in squareslist:
        goldbacknl.append(a+w)
goldbacknl = list(set(goldbacknl))
ansnum = None

for q in oddcompnumlist:
    if q  not in goldbacknl:
        ansnum = q
        break
print(ansnum)
