import time
#Brute-Force; will come up with a better solution later. Anything Above 6 will take very long.
#6 digits takes 1.3 seconds in python3
def getlucky(N):        # Haha get it? 'Get Lucky' by Daft Punk and others.....you know what? Nevermind.
    begin = time.time()
    delim = ''
    lastnum = delim.join([str(9)]*N)
    counter = 0
    for i in range(0,int(lastnum)+1):
        i = list(str(i).rjust(N,str(0)))
        i = [int(j) for j in i]
        if sum(i[:int(len(i)*0.5)])==sum(i[int(len(i)*0.5):len(i)]):
            counter += 1
    end = time.time()
    print("Time taken by brute force: "+str(end-begin))
    return counter


