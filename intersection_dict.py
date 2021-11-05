MY_SET={12,45,9,67,8}
MY_SET2={13,45,12,8}
print("l'intersection est:",MY_SET.intersection(MY_SET2))#pour afficher l'intersection
print("la differrence est:",MY_SET.difference(MY_SET2))
MY_SET=MY_SET.difference(MY_SET2)#pour supprimer les élément de l'intersections
print("le nevau set est:",MY_SET)
