# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 15:56:30 2021

Description : Ce programme calcule le taux de croissance annuelle en prenant en compte les valeurs 
d'investissement initiales et finals et la durée entre ces deux valeurs.L'utilisateur interagit avec 
une interface à travers laquelle il peut entrer ses données et recevoir le résultat en fonction 
de celles-ci.
Nous avons créé une interface en utilisant le modul tkinter, pour rendre l'utilsation agreable. 
Les entrées , c'est à dire les données sont verifiées de manière à forcer l'utilsateur à entrer un nombre 
entier positif.

@author: Team STARS RobotsMAli
version : 1.0.0


"""





from tkinter import * # l'importation  des methode du module tkinter // interface  





def conversionEnAnnee(ans, semaines, jours):
	"""
	conversionEnAnnee est une methode qui cnverstit les données en années

	ans 	  : le nombre de d'années

	semaine   : le nombre de semaines 
	jours     : le nombre de jours
	"""
	annees= ans + (((semaines*7) +jours)/365)

	return annees

def calculTauxCroissanceAnnuelle(valeurInitiale, valeurFinale, annees):
	"""
	calculTauxCroissanceAnnuelle est une fonction qui calcul le taux de croissance annuelle.

	valeurInitiale     :  la valeur valeur initiale
	valeurFinale 	   :  la valeur finale
	annees             :  le nombre d'années  
	"""
	
	#Decomposition  du calcul du taux de de croissance

	tauxDeCroissanceAnnuel = (valeurFinale/valeurInitiale)   #  Valeur finale divisée par valeur initiale = R1
	tauxDeCroissanceAnnuel **=(1/annees)        # R1 à la puissance de  l'inverse de  du nombre d'années = R2   
	tauxDeCroissanceAnnuel-=1   				   # R2 -1  = R3
	tauxDeCroissanceAnnuel *=100                # R3 multiplié par 100 = taux de croissance

	
	return round(tauxDeCroissanceAnnuel,3)

def Verification(V,F,A,S,J) : 
      """ 
      Verificaton est une fonction de vericatin des données entré l'utlisateur de l'interface. 
      Elle verifie si les données sont de type : nombre entier naturel.
      Elle genere une erreur dans une fenetre si les données ne sont pas correctes.
      Apres la verification des données, si les données sont correctes, elle les passe
      a des fonction de calcule. 
      
      V :  valeur initiale 
      F :  valeur finale
      A :  nombre d'années
      
      S :  nombre de semaines 
      J :  nombre de jours
         
      """
    
     
      # test du type
      if (not (V.isdigit())) or (not F.isdigit()) or (not A.isdigit()) or (not J.isdigit())  or (not S.isdigit()):
           # Dans le cas ou l'une des données n'est pas un entier positif 
           fenetre  = Tk()      # creation de fenêtre // fenetre d'erreur 
           fenetre.title("CALCULATRICE DE TAUX DE CROISSANCE ANNUELLE") # titre de la fenêtre
           fenetre.configure(bg="tan")
           fenetre.geometry("300x500") # dimension de la fenêtre
           fenetre.maxsize(width=300,height=100)# taille maximum
           error = Label(fenetre,text="ERREUR DE DONNEES",bg="chocolate",fg="black",width=500,height=2) # label d'error
           error.pack() 
           message = Label(fenetre,bg="tan",text=" Les données doivent être des nombres entiers positifs!")# label du message d'erreur
           message.pack()
           OK = Button(fenetre,text = "OK",command = fenetre.destroy)# button pour quitter la fenêtre d'erreur 
           OK.pack()
           fenetre.mainloop() # affichage de la fenêtre
           
      else : # si les données sont valides 
          print("OK")
          # Conversion en int 
          initialV = int(V)
          finaleV = int(F)
          annees = int(A)
          
          semaine  = int(S)
          jours = int(J)
          
          #appel des fonction de calcule
          nbreAns = conversionEnAnnee(annees,semaine,jours)
          tauxCroissance = calculTauxCroissanceAnnuelle(initialV, finaleV, nbreAns)
          
          
          resultat = Tk()
          
          resultat.title("TAUX DE CROISSANCE") # titre de la fenêtre
          resultat.configure(bg="tan")
          resultat.geometry("300x500") # dimension de la fenêtre
          resultat.maxsize(width=300,height=100)# taille maximum
          mes = Label(resultat,text="Le taux de croissance est : ",bg="chocolate",fg="black",width=500,height=2) # label d'error
          mes.pack() 
          res = Label(resultat,text=str(tauxCroissance)+"%",bg="tan")# label du message d'erreur
          res.pack()
          quitter = Button(resultat,text = "fermer",command = resultat.destroy)# button pour quitter la fenêtre d'erreur 
          quitter.pack()
          resultat.mainloop() # affichage de la fenêtre
        
          
          


def getEntry() : 
    """
    getEntry est une fonction de récuperation des données entrées par l'utilisateur.
    
    """
       
    ValeurInitiale = valeur_Initiale.get() # Récuperation de la valeur initiale dans le champ
   
   
    ValeurFinale = valeur_Finale.get() # Récuperation de la valeur finale dans le champ
    NbreAnnees = Nombre_Annee.get() # Récuperation du nombre d'années dans le champ
   
    NbreSemaine = Nombre_Semaine.get()#Rrécuperation du nombre de Semaines
    NbreJour = Nombre_Jour.get()# Récupération du nombre de jours dans le champ
    
    
    Verification(ValeurInitiale,ValeurFinale,NbreAnnees,NbreSemaine,NbreJour) 


#*******************************************PRINCIPALE*********************************    
    
ecran = Tk()        # Creation de fenetre principale 
ecran.title("Calculatrice de taux de croissance annuelle ")    # Titre de la fenêtre 
ecran.geometry("300x500") 
ecran.configure(bg="tan")      # Taille de la fenêtre
ecran.maxsize(width=300,height=530)       #  taille maximum de la fenetre 
entete = Label(text="CALCULATRICE DE TAUX DE CROISSANCE ANNUELLE",bg="chocolate",fg="black",width=500,height=2) #   Entête
entete.pack()
valeurI_Label = Label(ecran,text="Valeur initiale",bg="tan")      # Label de la valeur initiale 
valeurF_Label = Label(ecran,text="Valeur finale",bg="tan")        # Label de la valeur finale 
year_Label = Label(ecran,text="Nombre d'annees",bg="tan")         # Label du nombre d'années
semaine_Label = Label(ecran,text="Nombre de Semaines",bg="tan")   # Label du nombre de semaines
jour_Label = Label(ecran,text="Nombre de jour",bg="tan")          # Label du nombre de jours
valeurI_Label.place(x=15,y=70)      # Emplacement du Label valeur initiale
valeurF_Label.place(x=15,y=140)     # Emplacement du Label valeur finale 
year_Label.place(x=15,y=210)        # Emplacement du Label nombre d'années 
semaine_Label.place(x=15,y=280)     # Emplacement du Label nombre de semaines 
jour_Label.place(x=15,y=350)        # Emplacement du Label nombre de jours 


valeur_Initiale  = Entry(ecran,width=30) # Champ de valeur initiale
valeur_Finale = Entry(ecran,width=30)    # Champ de valeur finale
Nombre_Annee = Entry(ecran,width=30)     # Champ de nombre d'années

Nombre_Semaine = Entry(ecran,width=30)   # Champ de nombre de semaines
Nombre_Jour = Entry(ecran,width=30)      # Champ de nombre de jours 
valeur_Initiale.place(x=15,y=90)         # Emplacement du champ valeur initiale
valeur_Finale.place(x=15,y=160)          # Emplacement du champ  valeur finale
Nombre_Annee.place(x=15,y=230)           # Emplacement du nombre de d'années
Nombre_Semaine.place(x=15,y=300)         # Emplacementdu nombre de semaine
Nombre_Jour.place(x=15,y=370)            # Emplacement du nombre de jours
soumettre = Button(ecran,fg="black",width="30",height = "3",text="        Soumettre      ",command=getEntry) # Button de soumission des données
soumettre.place(x = 15,y=400)    # Emplacement du button de soumission 
fermer = Button(ecran,fg="black",width="30",height = "3", text="fermer",command=ecran.destroy)
fermer.place(x=15,y=460)





ecran.mainloop()            # Affichage de la fenêtre principale
