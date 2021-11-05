def som_recu(n):
    if (n <= 1 ):
        return n
    else:    
        return ( som_recu( n-1 ) + n )
n=int(input("entrez le nombre : "))
print(som_recu(n))
     