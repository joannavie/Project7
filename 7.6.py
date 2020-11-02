# -*- coding: utf-8 -*-
"""
Created on Sat May  2

@author: joannna prassa
###Άσκηση 7.6

"""
#Δημιουργώ το ζητούμενο λεξικό
dict2={'Rachel':'rch12','Monica':'mnc34','Joey':'jy56','Phoebe':'phb78','Chandler':'chndr54','Ross':'rss90'}

#Μεταβλήτη που θα μετράει προσπάθειες
n=0

#Εμφανίζω μήνυμα για να ενημερώσω τον χρήστη για των αριθμό των προσπάθειων
print("Διαθέτεις 3 προσπάθειες δοκιμών !")

#Ξεκινώ την επανάληψη
while (n < 3):
    #Ζητώ απο τον χρήστη το username
	username=input("Δώσε το username: ")
	#Αν το username που δίνει ο χρήστης δεν υπάρχει στο λεξικό, εμφανίζει μήνυμα 
	if username not in dict2:
		print(f"Το username που έδωσες είναι λανθασμένο")
		n+=1
	else:	
		#Ζητώ απο τον χρήστη τον κωδικό
		password=input("Δώσε το password: ")
        #Εάν ο κωδικός είναι σωστός τότε η είσοδος γίνεται με επιτυχία
		if password == dict2[username]:
			print("Επιτυχής είδοσδος")
			break
        #Εάν είναι λανθασμένος εμφανίζει μήνυμα
		else:
			print("Ο κωδικός που έδωσες είναι λανθασμένος .")
        
			
		
input()		