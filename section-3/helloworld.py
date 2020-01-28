
#Print function and concatenation
print('1- Hello','World!')
print('2- Hello World!')
print("3- 'Hello World!'")
print('4- "Hello World!"')
print("5- Hello World!")
print("6- Hello" + "World")


#Operators
print(" 5 + 1 =", 5 + 1)
print(" 5 - 1 =", 5 - 1)
print(" 5 * 1 =", 5 * 1)
print(" 5 / 1 =", 5 / 1)
print(" 5 % 1 =", 5 % 1)
print(" 5 // 1.5 =", 5 // 1) #Integer division

#Strings
print("Today is a good day to learn Python")
print('Python is fun')
print("Python's string is easy to use")
print('We can even include "quotes" in strings')
print('We can concate'+'nate too')
print('Escape character \nbreaks a line\n\n\nor a few')
print("You\tcan\ttab\tit. Tabs are 5 spaces long.")
#the slash \ redenrs a " or ' inside a string as a character
print('The pet show owner said "No, no, \'e\'s uh, ...he\'s resting".')
print("The pet show owner said \"No, no, \'e\'s uh, ...he\'s resting\".")
#then it comes the triple quotes to the rescue. You can even have it in multiple lines
print(""" 

Pet shop owner said: "No, no, 'e's uh, ...he's resting. 

""")

#You can break it into multiple lines but without actually breaking it
print("""This line \
was actually bro\
ken into mutiple \
lines.""")

#Backslash to the recue
print("C:\\Users\\times\\notes.txt")
#or this one r-> RAW STRING
print(r"C:\Users\times\notes.txt")


#Variables
greetings = 'Hello'
name = 'World ' 
age = 34

#Variables are bound to a value
print(type(greetings))
print(type(age))

age = "Can be bound to a string at any time"
print(type(age))

print(greetings, name)
#name = input('What is your name?')
print(greetings, name)

#Python is strongly typed

age = 34
name = "Melchiades"

#print(name + ' is ' + age + ' years old.')
#Give an str  - int error.

#Numeric Data types
#Integer, Float
Integer = 34
Float = 34.5
Decimal = 34.5

print(type(age))
