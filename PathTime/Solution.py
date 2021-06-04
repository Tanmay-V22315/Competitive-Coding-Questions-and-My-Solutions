initpos = [0,0]
coordcache = [[0,0]]
counter = 0
def movement(inpu):
    global counter
    if inpu=='N':
        newcoord = [initpos[0],initpos[1]+1]
        if newcoord in coordcache:
            counter += 1
        else:
            initpos[1]=initpos[1]+1
            coordcache.append(initpos)
            counter+=2
    if inpu=='S':
        newcoord = [initpos[0],initpos[1]-1]
        if newcoord in coordcache:
            counter += 1
        else:
            initpos[1]=initpos[1]-1
            coordcache.append(initpos)
            counter+=2
    if inpu=='E':
        newcoord = [initpos[0]+1,initpos[1]]
        if newcoord in coordcache:
            counter += 1
        else:
            initpos[0]=initpos[0]+1
            coordcache.append(initpos)
            counter+=2
    if inpu=='W':
        newcoord = [initpos[0]-1,initpos[1]]
        if newcoord in coordcache:
            counter += 1
        else:
            initpos[0]=initpos[0]-1
            coordcache.append(initpos)
            counter+=2
def solution(Strinp):
    for i in Strinp:
        movement(i)
    return(counter)
