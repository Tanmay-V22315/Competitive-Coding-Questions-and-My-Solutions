#Brute-Force; will come up with a better solution.
def getlucky(N):        # Haha get it? 'Get Lucky' by Daft Punk and others.....you know what? Nevermind.
    delim = ''
    lastnum = delim.join([str(9)]*N)
    counter = 0
    for i in range(0,int(lastnum)+1):
        i = list(str(i).rjust(N,str(0)))
        i = [int(j) for j in i]
        if sum(i[:len(i)//2])==sum(i[len(i)//2:len(i)]):
            counter += 1
    return counter
