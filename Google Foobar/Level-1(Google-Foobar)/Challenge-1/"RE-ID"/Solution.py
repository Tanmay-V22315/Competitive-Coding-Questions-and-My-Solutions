def solution(i):
    i = abs(int(i))
    # Brute-force for initial primes. Increase the upper-limit for range in the very first for-loop. You're gonna want to increase this for larger numbers as well as the upper-limit in complist.extend and primrange (Upper-limit number is not included in range).
    primlist = []
    randlist = []
    for j in range(2,142):
        boolist = []
        for k in range(2,j):
            if j%k != 0:
                boolist.append('false')
            elif j%k == 0:
                boolist.append('true')
                break
        if len(boolist) < j-2:
            randlist.append(j)
        else:
            primlist.append(j)
            randlist.append(j)
    # Sieve of Eratosthenes: Remove multiples of primes upto a prime number from a given range defined by i (Input) (Faster, smaller and overall much more efficient)
    complist = []
    for m in primlist:
        complist.extend(range(2*m,21000,m))
        complist.append(m**2)
    complist = list(set(complist))
    complist.sort()
    primrange = range(2,21000)
    for s in complist:
        primrange.remove(s)
    delim =''
    primstring = delim.join(map(str,primrange))
    indlist = list(primstring)
    indlist = indlist[i:i+5]
    ID = (delim.join(map(str,indlist)))
    return(ID)
#I realize that this code is way too long and complex for the simple thing it is supposed to do, But given that I'm still learning python, I'm quite proud of this actually.
#Takes 0.16 to 0.18 seconds to complete (At least that's what time.time() says)
