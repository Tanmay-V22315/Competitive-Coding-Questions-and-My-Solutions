# This solution is absolutely terrible. Look at better_soluton.py

class NoNegatives(list):
    def __getitem__(self, index):
        if index < 0:
            raise ValueError("Index must be positive")
        else:
            return list.__getitem__(self, index)
def solution(src,dest):
    src = int(src)
    dest = int(dest)
    currentloc = src
    univset = range(0,64)

    rowslist = NoNegatives([])
    for i in range(0,len(univset),8):
        rowslist.append(univset[i:i+8])

    rowslist = NoNegatives(rowslist)
    def getcoord(cloc):
        global x
        global pos
        for x in range(0,len(rowslist)):
            try:
                pos = rowslist[x].index(cloc)
                break
            except:
                pass
        return(pos,x)
    def getnum(xcord,ycord):
        return(rowslist[ycord][xcord])
    def coordcompare((pos1,x1),(pos2,x2)):
        distance = ((pos2-pos1),(x2-x1))
        return(distance)
    def downleft(acord):
        getcoord(acord)
        try:
            landnumdl = rowslist[(x+2)][abs(pos-1)]
            coordsdl = getcoord(landnumdl)
            return(landnumdl,coordsdl)
        except:
            pass
    def downright(acord):
        getcoord(acord)
        try:
            landnumdr = rowslist[x+2][pos+1]
            getcoord(landnumdr)
            coordsdr = (pos,x)
            return(landnumdr,coordsdr)
        except:
            pass
    def rightdown(acord):
        getcoord(acord)
        try:
            landnumrd = rowslist[x+1][pos+2]
            getcoord(landnumrd)
            coordsrd = (pos,x)
            return(landnumrd,coordsrd)
        except:
            pass
    def leftdown(acord):
        getcoord(acord)
        try:
            landnumld = rowslist[x+1][abs(pos-2)]
            getcoord(landnumld)
            coordsld = (pos,x)
            return(landnumld,coordsld)
        except:
            pass
    def rightup(acord):
        getcoord(acord)
        try:
            landnumru = rowslist[x-1][pos+2]
            getcoord(landnumru)
            coordsru = (pos,x)
            return(landnumru,coordsru)
        except:
            pass
    def leftup(acord):
        getcoord(acord)
        try:
            landnumlu = rowslist[abs(x-1)][abs(pos-2)]
            getcoord(landnumlu)
            coordslu = (pos,x)
            return(landnumlu,coordslu)
        except:
            pass
    def upleft(acord):
        getcoord(acord)
        try:
            landnumul = (rowslist[x-2][abs(pos-1)])
            getcoord(landnumul)
            coordsul = (pos,x)
            return(landnumul,coordsul)
        except:
                pass
    def upright(acord):
        getcoord(acord)
        try:
            landnumur = (rowslist[x-2][pos+1])
            getcoord(landnumur)
            coordsur = (pos,x)
            return(landnumur,coordsur)
        except:
            pass
    def layergen(boardnum):
        global coordslist
        coordslist = []
        try:
            coordslist.append(upleft(boardnum)[0])
        except:
            pass
        try:
            coordslist.append(upright(boardnum)[0])
        except:
            pass
        try:
            coordslist.append(leftdown(boardnum)[0])
        except:
            pass
        try:
            coordslist.append(leftup(boardnum)[0])
        except:
            pass
        try:
            coordslist.append(downright(boardnum)[0])
        except:
            pass
        try:
            coordslist.append(downleft(boardnum)[0])
        except:
            pass
        try:
            coordslist.append(rightup(boardnum)[0])
        except:
            pass
        try:
            coordslist.append(rightdown(boardnum)[0])
        except:
            pass
        return(coordslist)
    stepnum = 0
    moveslist = NoNegatives([src])
    moveslistbuf = []
    moveslistbuf2 = []
    currentloc = src
    while currentloc != dest:
        for i in moveslist:
            currentloc = i
            moveslistbuf.append(layergen(i))
        for i in moveslistbuf:
            moveslistbuf2 += i
        if dest in moveslistbuf2:
            currentloc = moveslistbuf2[moveslistbuf2.index(dest)]
        moveslist = NoNegatives(moveslistbuf2)
        stepnum = stepnum+1
    return(stepnum)
