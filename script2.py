#!/bin/Python3
import sys #system functions and parameters
#Importing
#sys modules-modules that affect system functions and parameters

print(sys.version)

#argv - arguments

from datetime import datetime as dt #import with alias
print(dt.now())



#Advance Strings

my_name = "Frederick"
print(my_name[0])
print(my_name[-1])


sentence = "Esto es una oracion."
print(sentence[:4])

print(sentence.split())

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "El dijo, \"gimme todo su dinero!\'"
print(quote) #this is example of character escaping

too_much_space = "        hi             "
print(too_much_space.strip())     

letter = "A"
word = "Apple"
print("A" in "Apple")
print(letter.lower() in word.lower()) #improved

movie = "The Hangover"
print("my favorite movie is {}.".format(movie))
 # note the brackets (not parenthesis)
 #this method better than concatenating it (1st video)
 
 

 #Dictionaries  key/value pairs {}
 
drinks = {"Tequila Sunrise": 7, "Bloody Mary": 10, "Rum n Coke": 8} #this is a dictionary, drink is your key, price is the value
print(drinks)
 
employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy", "Mort"]}
print(employees)

employees["Legal"] = ["Mr. Frond"] #adding new key:value pair
print(employees)

employees.update({"Sales": ["Andie", "Ollie"]})
#alternate way to add new key value pairs
print(employees)


#this not really used in course but bueno a saber

#Sockets  they can connect 2 nodes juntos

#this was done in seperate file, it is the beginning of the next video, the port scanner


