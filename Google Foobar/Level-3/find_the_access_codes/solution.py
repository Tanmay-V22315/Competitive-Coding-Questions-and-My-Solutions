def solution(l):
    # Your code here
    res=[]
    for i in l:
        current_i_index=l.index(i)
        for j in l[current_i_index+1:]:
            if j%i!=0:
                break
            else:
                current_j_index=l.index(j)
                for k in l[current_j_index+1:]:
                    if k%j==0 and [i,j,k] not in res:
                        res.append([i,j,k])
    return len(res)
                        
