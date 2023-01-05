#!/bin/python3




#Variables and Methods

quote = "Defeat is never shameful but better you than me."
print(quote.upper()) #upper command prints output as uppercase
print(quote.lower()) #lowercase
print(quote.title()) #titlecase

print (len(quote))

name = "Frederick Taylor" #String
age = 40 #integer (has no decimal point)
gpa = 3.7 #float   (has decimal point

print(int(age))
print(int(40.2))

#Below syntax is wrong because "age is designated as an integer"
#you cant concatenate a string with an integer
#print("Mi nombre es " + name + " y estoy " + age + " anos de edad)

#syntax below is correct, made it a string ((str(age)
print("Mi nombre es " + name + " y estoy " + str(age) + " anos de edad")

#below adds one to age variable
age += 1
print(age)

birthday = 1
age += birthday
print(age)



print('\n')



#Functions
print("Esto es un ejemplo")


def who_am_i(): #this is a function
	name = "Frederick"
	age = 40
	print("Mi nombre es " + name + " y estoy " + str(age) + " anos de edad")
	
who_am_i() #this "calls" the function, above code does nothing without this




#adding parameters

def add_one_hundred(num):
	print(num + 100)
	
add_one_hundred(100)


#multiple parameters
def add(x,y):
	print(x+y)
	
add(7,7)


def multiply(x,y):
	return x * y
	
print(multiply(7,7))


def square_root(x):
	print(x ** .5)
square_root(64)


def nl():
	print('\n')
	



nl()
#Boolean Expressions (cierto o falso)
print("Boolean expressions:")

bool1 = True
bool2 = 3*3 ==9
bool3 =False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

# "true" is a string, true is boolean. with quotes is string, w/o is bool


nl()
#Relational y Boolean Opperators
greater_than =7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

test_and = (7 > 5) and (5 < 7 ) #true
test_and2 = (7 > 5) and (5> 7) #false
test_or = (7 > 5) or (5 < 7) #true
test_or2 = (7 > 5) or (5 > 7) #true
# 'and' requires BOTH statements be true to be considered true, (otherwise its false)
# while 'or' requires only one of them be true to be considered true
test_not = not True #false

#looked up "truth charts" on Google

#didnt do that myself but perhaps in future, kinda ya feel comfortable



#Conditional Statements (if, else)
def drink(money):
	if money >= 2:
		return "You've got yourself a drink, bien hecho!!"
	else:
		return "NO drink for you, nothing personal just business."

print(drink(3))
print(drink(1))


#('age, money' are the parameters)
def alcohol (age,money) :
	if (age >= 21) and (money >= 5):
		return "Yay! A drink!!"
	#(elsf means 'else if')
	elif  (age >= 21) and (money < 5):
		return "Need more paper my dude."
	elif (age < 21) and (money >= 5):
		return "No drink for you, foolish joven!!"
	else: 
		return "You're too poor and too young."
	
	
print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,4))
print(alcohol(19,3))


nl()
#Lists - lists live in brackets

movies = ["The Incredibles", "Kung Fu Panda", "Clone Wars, Madagascar"]


print(movies[1]) #return 2nd item, 
print(movies[0]) #returns 1st item, lists are counted starting from 0
print(movies[1:4])
print(movies[1:]) #this will pull EVERYTHING on list
print(movies[:1]) #print in reverse
print(movies[-1]) #will print last item
print(len(movies)) #length
movies.append("Spiderman") #add to list
print(movies) #now this print appened list


movies.pop() #delete last item on the list
print(movies) #again this prints out new change

movies.pop(0) #delete 1st thing on list
print(movies)

#lists have brackets, many ways to return items
#this is just a way to get familiar with syntax
#remember we count from 0, not 1



nl()
#Tuples 
# lists are "mutable"(they can be changed)
# Tuples are lists that CANNOT be changed ()
#lists have bracketts, tuples have parenthesis

grades = ("a", "b", "c", "d", "f")
#above is a tuple, parenthesis, not bracketts
#grade.pop or append will not work
print(grades[1]) #this wont work



nl()
#Looping

#For loops - start to finish of an iterate
veggies = ["cucumber", "spinach", "carrot"]
for x in veggies:
	print(x)
	
#While Loops - Wil execute as long as they're "true"

i = 1

while i < 10:
	print(i)
	i += 1
	
