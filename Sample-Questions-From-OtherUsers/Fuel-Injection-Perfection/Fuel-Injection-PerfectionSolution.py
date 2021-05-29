def solution(n):
	 #available operations = +1,-1,*0.5
    stepnum = 0
    while n !=1:
        if n%2==0: #If number is even, the most efficient way to bring it to one would be two continuously divide it by 2. Except when first division results in an odd number, which is handled by the else statement.
            n = n*0.5
            stepnum=stepnum+1
        else:
            addres = ((n+1)/2)%2 #\These two are important because they will help in determining whether addition or subtraction is more efficient.
            subres = ((n-1)/2)%2 #/
            if n<=3: #If n becomes three or two, subres would become 1 which is not divisible by 2 so the logic would proceed with adding a pellet which would introduce an unnecessary step, so this is the override for that. 
                n = n-1
                stepnum = stepnum+1
            elif subres == 0 and subres < addres:
                n = n-1
                stepnum = stepnum+1
            else:
                n=n+1
                stepnum = stepnum+1
    return(stepnum)
