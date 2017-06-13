#MODULES
import random #That's self explanatory too
from math import pi, sqrt #We can do this if we only need certain func(s) from a module
from math import sqrt as square_root #this imports sqrt under a diff name

#BASICS
print("meme")

5+4-3 
2*(3+4)

str1="This is a string"
"""This will create
a string wich goes to a new line everytime ENTER is pressed"""

input("enter something")

"2" # this is not an int, but a str

print(int("2")+3) #converts the "2" str to an int and processes it
float(input("Enter a number: ")) #Sets the input as the var value
del str1                    #Deletes the str1 var
print(str1)                 #Prints an error, since str1 has been deleted

"hello" == "hello" # == is a bool, wich returns True and False (watch out uppercase)
                            #/!\ = is an assignment while == is a bool

1 != 1 #Other type of bool, this will print false because it isn't not equal
'''
Then there is >, <, >=, <=, like in c#
'''

#LOOPS
if 10 > 5:                  #py's if doesn't use (),{}. Only :
   print("10 greater than 5")
else:                       #else is done the same way
    if 5>10:                #if/else statements can be nested indefinitely
    print("Wait what")
    else:
        print("That doesn't make any sense")

num = 7
if num == 5:
   print("Number is 5")
elif num == 11:             #We use elif(else if) because it is more practical than the above code
   print("Number is 11")
elif num == 7:
   print("Number is 7")
else:
   print("Number isn't 5, 11 or 7")

                            #if statements can be nested, as in any other language
num = 12
if num > 5:
   print("Bigger than 5")
   if num <=47:
      print("Between 5 and 47")
                        '''
                        py uses words for bool logic whereas other langs use &&, ||...
                        Those are: and (if both are true, then True, othw False)
                                   or (if 1+ is true, then True, othw False)
                                   not (Only takes 1 arg (not arg), True goes to False and vice versa)
                        '''
'''
py uses the same idea of order of operations than maths
(* and / before + and -, etc...)
'''
>>> False == False or True # == is more important than the or statement
True
>>> False == (False or True) #brackets do the same thing than in maths
False
>>> (False == False) or True
True


i = 1
while i <=5: #This while loop will count to 5 then stop
   print(i)
   i += 1

while 1==1:
  print("In the loop") #This is an infinite loop and would never stop running

i = 0
while 1==1:
  print(i)
  i = i + 1
  if i >= 5:
    print("Breaking")
    break                   #To stop a loop prematurely, we use the break statement

i = 0
while True:
   i = i +1
   if i == 2:
      print("Skipping 2")
      continue              #the continue statement moves onto the next iteration
   if i == 5:
      print("Breaking")
      break
   print(i)

print("Finished")


#LISTS
words = ["Hello", "world", "!"] #Lists are basically arrays
print(words[0])
print(words[1])
print(words[2])

number = 3
things = ["string", 0, [1, 2, number], 4.56] #A list can contain items of multiple types
print(things[1])
print(things[2])
print(things[2][2]) #Lists can be nested (this will print 3

nums = [7, 7, 7, 7, 7]
nums[2] = 5
print(nums)

>>>[7, 7, 5, 7, 7]

nums = [1, 2, 3]    #Lists can be added an multiplied the same way as str s
print(nums + [4, 5, 6])
print(nums * 3)

words = ["spam", "egg", "spam", "sausage"]
print("spam" in words) #This will return a bool(True itc) that checks if the item is in the list

nums = [1, 2, 3]
nums.append(4)  #This will add 4 at the end of the list
print(nums)

nums = [1, 3, 5, 2, 4]
print(len(nums))    #len prints the number of items in the list

words = ["Python", "fun"]
index = 1
words.insert(index, "is") #similar to append, but lets you insert the item at the index you want
print(words)

'''
There are a few more useful functions and methods for lists. 
max(list): Returns the list item with the maximum value
min(list): Returns the list item with minimum value
list.count(obj): Returns a count of how many times an item occurs in a list
list.remove(obj): Removes an object from a list
list.reverse(): Reverses objects in a list
'''

numbers = list(range(10)) #range creates a sequential list of numbers
print(numbers)
>>>[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers = list(range(3, 8)) # This will range all ints from 3 to 8 (2 args)
print(numbers)

print(range(20) == range(0, 20))

numbers = list(range(5, 20, 2)) #range can hava a trid arg, wich determines the interval of the sequence
print(numbers)
>>>

words = ["hello", "world", "spam", "eggs"]
for word in words:    #the for loop goes through all items in a list (= foreach)
  print(word + "!")[5, 7, 9, 11, 13, 15, 17, 19]

for i in range(5): #A range can be used to repeat the action x times
print("hello!")   #It doesn't need to be listed aw we don't use the indexes


#FUNCTIONS
def my_func(): #def initiates a func
  print("spam") #funcs must be initiated BEFORE the call
  print("spam")
  print("spam")

my_func() #call to the func

def print_with_exclamation(word): #funcs can also take arguments
   print(word + "!")
    
print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")

excla = print_with_exclamation #funcs can be assigned like any other object
print(excla("meme"))

def print_sum_twice(x, y): #And multiple args as any other lang :^)
   print(x + y)
   print(x + y)

print_sum_twice(5, 8)

def function(variable): #func args can be declared as vars
   variable += 1
   print(variable)

function(7)


def max(x, y): 
    if x >=y:
        return x  #That's pretty self explanatory
    else:
        return y  #return ends the punction, so any code after the return statement will be ignored
        
print(max(4, 7))
z = max(8, 5)
print(z)


def add(x, y):
  return x + y

def do_twice(func, x, y): #hey can also be used as args
  return func(func(x, y), func(x, y))

a = 5
b = 10

print(do_twice(add, a, b))

value = random.randint(1, 6) #this uses the imported module, see on top


#EXCEPTIONS
try:  #self ex
   num1 = 7
   num2 = 0
   print (num1 / num2)
   print("Done calculation")
except ZeroDivisionError: #Error handling
   print("An error occurred")
   print("due to zero division")
   except (ValueError, TypeError): #mutliple except blocks can be used
   print("Error occurred")         #And have mutliple errors to handle
  except:         #An except block without defined excep will catch all of them
   print("An error occurred")
finally:  #Basically a "default" that will run no matter what
   print("This code will run no matter what")
   raise ValueError("This is a test") #This will raise the value error
   #You can give details about the exces by putting it into arg

   try:
   num = 5 / 0
except:
   print("An error occurred")
   raise #Raise without args can be used to re raise whatevs exce occured
>>>
An error occurred

ZeroDivisionError: division by zero


#FILES
myfile = open("filename.txt") #Before editing a text file, we need to open it

'''
You can specify the mode used to open a file by applying a second argument to the open function.
Sending "r" means open in read mode, which is the default. 
Sending "w" means write mode, for rewriting the contents of a file.
Sending "a" means append mode, for adding new content to the end of the file.

Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files).
'''
myfile2 = open("afile.txt", w) #read only is the default mode
# do stuff to the file
myfile2.close() #When we're done with the file, we need to close it

file = open("filename.txt", "r") #Reading files
cont = file.read() #Const is now the whole file's content
print(cont)
file.close()

file = open("filename.txt", "r")
print(file.read(16)) #We can passthe number of bytes we want to read as an arg
print(file.read(4)) #More calls = more of the file by x bytes
print(file.read(4))
print(file.read()) #This prints the rest of the file
file.close()  #If you try to read th file after it's done reading, it will return an empty string

file = open("newfile.txt", "w") #The w mode creates a file if it doesn't exist
file.write("This has been written to a file") #This writes, lul
file.close()

#When a file is opened in read mode, it's contents is deleted

'''
It is good practice to avoid wasting resources by making sure that files are always
closed after they have been used. One way of doing this is to use try and finally.
This ensures that the file is always closed, even if an error occurs.
'''
try:
   f = open("filename.txt")
   print(f.read())
finally:
   f.close()
'''
An alternative way of doing this is using with statements.
This creates a temporary variable (often called f),
which is only accessible in the indented block of the with statement.

The file is automatically closed at the end of the with statement,
even if exceptions occur within it.
'''
with open("filename.txt") as f:
  print(f.read())

#>>>>>>the None object is similar to null in other langs

#DICTIONNARIES