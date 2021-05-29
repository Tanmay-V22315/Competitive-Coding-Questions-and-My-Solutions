def solution(x, y):
    yval = int(0.5*y*y-0.5*y+1)
    a=0.5
    b = y-0.5
    c = int(yval-(a+b))
    xval = int(a*x*x+b*x+c)
    return(str(xval))
