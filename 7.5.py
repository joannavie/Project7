# -*- coding: utf-8 -*-
"""
Created on Sat May  2 

@author: joannna prassa
###Άσκηση 7.5

"""
#Εφόσον δεν εχει υλοποιηθεί το ζητούμενο λεξικό δημιουργώ εγω ένα
lexiko={1:1,2:1.41,3:1.73,4:2,5:2.23,6:2.44,7:2.64,8:2.82}
print("Το αρχικό λεξικό είναι:\n",lexiko)

#Δημιουργώ μια κενή λίστα για να προσθέσω τα στοιχεία
alist=[]

sum = 0

#Ξεκινώ την επανάληψη
for i in lexiko:
    
    #Προσθέτω το κλειδί με την τιμή του
    sum = i + lexiko[i]
    
    #Κάνω προσθήκη των τιμών στην λίστα 
    alist.append(sum)
    


#Εμφανίζω την λίστα που δημιουργήθηκε    
print("Η λίστα που δημιουργείται είναι:\n",alist)

input()