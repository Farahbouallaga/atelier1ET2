def selection(tab):
    for i in range(len(tab)):
        min = i	
        for j in range(i+1, len(tab)):
           if tab[min] > tab[j] :
               min = j
               p = tab[i]	
               tab[i] = tab[min]
               tab[min] =tmp
    return tab
# tri par insertion
def insertion(tab): 
    for i in range(1, len(tab)): 
        k = tab[i] 
        j = i-1
        while j >= 0 and k < tab[j] : 
                tab[j + 1] = tab[j] 
                j = j- 1
        tab[j + 1] = k
    return tab

#tri a bull
def bull(tab):
    n = len(tab)
    for i in range(n):
        for j in range(0, n-i-1):
            if tab[j] > tab[j+1] :
                tab[j]  = tab[j+1] 
                tab[j+1] =tab[j]
    return tab 

tab=[4,5,10,2,15,1,3,-12 ,0]
print(selection(tab))
print(insertion(tab))
print(bull(tab))
