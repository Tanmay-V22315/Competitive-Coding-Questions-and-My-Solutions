def knight(src,dest):
    def convert(representation):
        try:
            if type(representation)==int:
                assert 0<=representation<=64, "Number is out of bounds!"
                return representation-(representation//8)*8,representation//8

            elif type(representation)==tuple:
                assert 0<=representation[0]<=8 and 0<=representation[1]<=8, "Coordinates are out of bounds!!"
                return representation[1]*8+representation[0]
            
            elif type(representation)==str:
                return convert((ord(representation[0])-97, int(representation[1])-1))
        except:
            return None
    if type(src)==str: src=convert(src)
    if type(dest)==str: dest=convert(dest)        
    def movement(src):
            if type(src)==int: src=convert(src)
            assert type(src)==tuple
            numbers_to_be_appended=[(src[0]+1, src[1]-2),(src[0]-1, src[1]-2),(src[0]+1, src[1]+2),(src[0]-1, src[1]+2),(src[0]-2, src[1]+1),(src[0]-2, src[1]-1),(src[0]-2, src[1]+1),(src[0]-2, src[1]-1),(src[0]+2, src[1]+1),(src[0]+2, src[1]-1)]
            return [convert(i) for i in numbers_to_be_appended if convert(i)!=None and 63>=convert(i)>=0 and 0<=i[0]<=7 and 0<=i[1]<=7]
    known_locations=[src]
    counter=0
    while dest not in known_locations:
        counter+=1
        temp=[]
        for i in known_locations:
            try: temp.extend(movement(i))
            except: pass
            temp=list(set(temp))
        known_locations.extend(temp)
        known_locations=list(set(known_locations))
    return counter