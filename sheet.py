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

words = ["Hello", "world", "!"] #Prints are basically arrays
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