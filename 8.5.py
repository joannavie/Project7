# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 13:41:45 2020

@author: Joanna Prassa
## Άσκηση 8.4
"""
#Δημιουργώ την συνάρτηση που μετατρέπει την θερμοκρασία απο κελσίου σε φαρενάιτ
def convert_temp(clist,n):
     
     Fahrenheit = []
     for i in range (0,n):
         
         item = 9.0/5.0 * clist[i] + 32
         Fahrenheit.append(item)
         
     return Fahrenheit


#Ζητάω απο το χρήστη να δώσει το πλήθος των βαθμών κελσίου
n=int(input("Δώσε το πλήθος των βαθμών κελσίου που θα δώσεις :"))
celsius_list = []
#Καταχωρώ τους βαθμούς που θα δώσει ο χρήστης σε λίστα
for i in range(0,n):
    celsius_degree = float(input("\nΔώσε μια θερμοκρασία σε βαθμούς κελσίου: "))
    celsius_list.append(celsius_degree)
    
#Καλώ την συνάρτηση 
f_list = convert_temp(celsius_list,n) 

#Εμφανίζω τα αποτελέσματα
print ("Η αρχική λίστα με τους βαθμούς κελσίου είναι :")  
print(celsius_list)

print("Η λίστα σε Φάρεναιτ είναι :")
print(f_list)
 