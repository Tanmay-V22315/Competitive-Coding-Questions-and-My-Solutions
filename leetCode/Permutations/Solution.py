def main(x):
    for i in x:
        x[x.index(i)]=str(i)
    z="".join(x)
    
    