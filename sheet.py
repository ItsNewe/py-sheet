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
                        py uses word for bool logic whereas other languages use &&, ||...
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