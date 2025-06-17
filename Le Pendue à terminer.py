nombre_de_point = 7
les_point =0

#la mise en place du jeu :
# récupération du mot:
la_mot = input ("Player 1 Choisit une mot : " )


    # Montré le nombre de lettre :
les_undescore = "_"*len(la_mot)
print (les_undescore )

# Des paramètre pour le code ci besoin : 
# liste_des_underscore.append (les_undescore)

# les_undescore=[les_undescore]
# liste_du_mot = []
# liste_du_mot.append (la_mot)
# print (type (liste_du_mot))
# print (liste_des_underscore)[0:1]




liste_des_underscore = []
liste_des_underscore.append (les_undescore)

    # Le début du jeu :
while True :

    la_question_pour_lettre = input ("Qu'elle va être ta lettre : ")
    if la_question_pour_lettre in la_mot[0:] : 
        print (f"bonne Réponse ")
        index = la_mot.index (la_question_pour_lettre)
        Index_1 = index+1        
        liste_des_underscore [index:Index_1] =  la_question_pour_lettre 
       


        print (f"Voicie la partie d mot que tu as découvert {liste_des_underscore}")



        # Calcul des points pour arrter le code quand le mot est trouvé 
        les_point += 1
        if les_point == len (la_mot) :
            print (f"Bravo tu as gagné le mot était bien {la_mot}")
            break
       
       
# ce qui se passe si le mot n'est pas bon :
    else : 
        nombre_de_point -= 1
        print (f"mauvaise réponse tu perd un point, il te reste: {nombre_de_point} de point" )
        if nombre_de_point == 0 : 
            print (f"Tu as perdu le  mot était : {la_mot}")
            break
