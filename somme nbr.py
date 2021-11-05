def somme(n):
    if (n==0):
        return 0
    else:	
        return n+somme(n-1)# LA FONCTION RECURCIVE
n=int(input("entrer un num"))
somme(n)
print("votre somme est",somme(n))# AFFICHAGE DE LA SOMME 
