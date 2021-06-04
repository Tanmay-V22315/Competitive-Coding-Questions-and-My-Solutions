def solution(x):
    memo = [None]*(x+1)
    try:
        memo[0],memo[1]=0,1
    except:
        pass
    def fib(n): #Using Memoization DP; takes much less time.
        if n==1 or n==0:
            return n
        if memo[n]!=None:
            return memo[n]
        else:
            memo[n]=fib(n-1)+fib(n-2)
        return(memo[n])
    def fibdac(n): #Using Divide and Conquer; takes longer for larger numbers.
        if n==1 or n==0:
            return n
        else:
            return fibdac(n-2)+fibdac(n-1)
    return fib(x)
print(solution(5))
