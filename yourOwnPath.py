def maze(N,road):
    solution=''
    for i in range(2*N-2):
        
        if road[i]=='E':
            solution=solution+'S'
        else:
            solution=solution+'E'
    return(solution)       
T=int(input('NUMBER OF TESTS'))


for j in range(T):
    N=int(input('DIMENSION'))
    road =input("LYDIA'S ROAD")
   
   
    print('case #',j+1, ': ',maze(N,road))
