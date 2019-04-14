def test_cases_number():
    T=0
    while not( T in range (1,101)):
        T=int(input('give me the number of test cases'))
        
       
    return(T)



def detect_digit(N):
    C=str(N)
    powers=[]
    B=0
 
    
    for i in range(len(C)):
        if C[i]=='4':
            powers.append(i)
            
    for j in range(len(powers)):
        B=B+2*10**(len(C)-1-powers[j])
    return(B)


def prize():
  N=0
  while str(N).find('4')==-1:
        N=int(input('Give a price value'))
  return(N)      


T=test_cases_number()
for k in range(T):
    N=prize()
    B=detect_digit(N)

    A=N-B
    print('case#'+str(k+1), A, B)
