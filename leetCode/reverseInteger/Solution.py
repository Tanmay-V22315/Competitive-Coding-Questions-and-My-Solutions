class Solution:
    def reverse(self, x: int) -> int:
        sign=0
        if x<0:
            sign=1
            
        unsigned=str(x).replace("-","")[::-1]
        
        if sign==1:
            signed=int("-"+unsigned)
        else:
            signed=int(unsigned)
        
        
        if abs(signed)>=(1<<31)-1:
            return 0
        else:
            return signed

        
