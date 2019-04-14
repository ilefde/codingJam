
def number_of_operations(N):
    S=A=int(N)
    B=N
    C=N
    a=0
    s=0
    i=0
    j=0
    while i<len(B):
        
       
        while int(B[i]) % 2:
            S=S-1
            s=s+1
            B=str(S)
           
        i=i+1
    while j<len(C):
        while int(C[j]) % 2:
            A=A+1
            a=a+1
            C=str(A)
        j=j+1
    m=min(a,s)         
    return(m)
            




N= input('give me a number')
print(number_of_operations(N))
