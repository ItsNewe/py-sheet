#MODULES
import random #Importe le module entier
from math import pi, sqrt #Préférable si on a besoin que de certaines fonctions d'un module
from math import sqrt as square_root #Importe sqrt() sous un autre nom

#BASES
print("meme")

5+4-3 
2*(3+4)

str1="Ceci est une string"
"""Ceci créé
une string qui va à la newline à chaque fois qu'on appuye sur ENTREE"""

input("Entrer une valeur") #Print le texte entre parenthèses dans la console et enregistre la valeur 
                           #qu'on tape comme valeur de la variable

"2" #Ce n'est pas un int, mais une string

print(int("2")+3) #Convertit 2 en int et effectue l'opération (sans la conversion, une erreur surviendrait)
value = float(input("Entrez un chiffre à virgule: ")) #Définit la valeur donnée comme la valeur de la variable, de type float
del str1                    #Supprime la var str1
print(str1)                 #Erreur, vu que str1 à été supprimée

"hello" == "hello" # == est un bool, qui renvoie True ou False (attention aux maj)
                            #/!\ "=" est un assignement tandis que "==" est un bool

var1 != var2 #Un autre type de bool, qui renvoie True si var1 n'est pas égal à var2 et inversement
'''
Il existe d'autres type de comparateurs (bool):
> : Renvoie True si var1 est plus grand que var2
< : Renvoie True si var1 est plus petit que var2
>= : Renvoie True si var1 est supérieur ou égal à var2
<= : Renvoie True si var1 est inférieur ou égal à var2

'''

#BOUCLES (LOOPS)
#LES BOUCLES IF

#Les boucles en python n'utilisent pas {}, py utilise l'identation (tabs) et les ":"
if 10 > 5:                    #En py, les parenthèses pour définir les variables d'une boucle sont optionelles
   print("10 est plus grand que 5") #(On peut écrire if(var1 == var2): comme on peut écrire if var1==var2:)
else:                       
    if 5>10:                #Les boucles if/else peuvent être nestés indéfiniment (nesté = boucle dans une boucle)
        print("Uhm..")
    else:
        print("J'ai beugé")

num = 7
if num == 5:
   print("Le nombre est 5")
elif num == 11:             #Utiliser "elif" au lieu de succéder les if() est plus pratique
   print("Le nombre est 11")
elif num == 7:
   print("Le nombre est 7")
else:
   print("Le nomnre n'est ni 5, ni 11, ni 7")

                            #On peut nester les boucles if comme dans n'mporte quel language
num = 12
if num > 5:
    print("Plus grand que 5")
    if num <=47:
      print("entre 5 et 47")
      '''
      py utilise des mots pour la logique booléenne là ou d'autres langages 
      utilisent "&&", "||", etc...
      Ces mots sont: 
      and = (Si les deux sont True; renvoie True)
      or = (Si au moins 1 arg est True; renvoie True)
      not = (Prend seulement 1 arg. Si la var est True; renvoie False et inversement)
      '''
'''
py utilise le même ordre de priorité qu'en maths
("*" & "/" avant "+" & "-")
'''
>>> False == False or True # "==" passe avant le "or"
True
>>> False == (False or True) #Comme en maths, les parenthèses sont prioritaires
False
>>> (False == False) or True
True

#LES BOUCLES WHILE

i = 1
while i <=5: #Une boucle while effectue l'action définie tant que la valeur renvoie True
   print(i) #Celle ci va compter jusqu'à 5 puis s'arrêter
   i += 1   #Ne pas oublier d'incrémenter 1 pour éviter une boucle infinie

while 1==1:
  print("Vers l'infini et au delà") #Cette boucle est une boucle infinie, car sa valeur restera toujours True

i = 0
while 1==1:
  print(i)
  i +=1
  if i >= 5:
    print("On sort de la loop")
    break                   #Pour sortir d'une boucle, on utilise "break"

i = 0
while True:
   i += 1
   if i == 2:
      print("On passe 2")
      continue              #"continue" laisse la boucle s'éxecuter 
   if i == 5:
      print("Sortie de la boucle")
      break
   print(i)

print("Terminé")

#LA BOUCLE FOR

words = ["hello", "world", "spam", "eggs"]
for word in words:    #La boucle for analyse tous les items que contient un élément
  print(word + "!")
>>>hello! world! spam! eggs!
for i in range(5): #Un range peut être utilisé pour effectuer une action x fois (comme un while)
  print("hello!")   #Pas besoin d'être listé et n'utilise pas les indexes


#LISTES

words = ["Hello", "world", "!"] #Une liste est une array dans les autres languages
#/!\ LE PREMIER INEDX D'UNE LISTE EST 0 ET NON 1
print(words[0]) #Pour accéder au premier élément d'une liste, on utilise donc [0]
print(words[1]) #Le chiffre entre crochet détermine la position de l'élément dans l'array
print(words[2]) #On appelle ce chiffre "l'index"

number = 3
things = ["string", 0, [1, 2, number], 4.56] #Une liste peut contenir des éléments de tous types
print(things[1])
print(things[2])
print(things[2][2]) #Les listes peuvent être nestés (ceci va print 3)

nums = [1, 2, 3, 4, 5]
nums[2] = 5 #Remplace "3" par "5"
print(nums)

>>>[7, 7, 5, 7, 7]

nums = [1, 2, 3]    #Les listes peuvent être concaténées, tout comme les str
print(nums + [4, 5, 6])
print(nums * 3)

words = ["spam", "egg", "spam", "sausage"]
print("spam" in words) #Cela retourne True si "spam" est trouvé dans la liste

nums = [1, 2, 3]
nums.append(4)  #La méthode append() va rajouter l'argument donné à la fin de la liste
print(nums)

nums = [1, 3, 5, 2, 4]
print(len(nums))    #len() print la longueur de l'élément, en l'occurence celle de la liste

words = ["Python", "fun"]
words.insert(1, "is") #Insère l'argument à l'index choisi, en l'occurence words[1]
print(words)
>>>["Python", "is", "fun"]
'''
Il existe un tas de fonctions pour les listes, en voici quelques unes: 
max(list): Renvoie l'élément de la liste ayant la plus grande valeur
min(list): Renvoie l'élément de la liste ayant la plus petite valeur
list.count(obj): Renvoie un int équivalent au nombre de fois qu'un item apparait dans la liste
list.remove(obj): Supprime un objet de la liste (Mettre en arg l'objet lui même, pas l'index)
list.reverse(): Mets la liste à l'envers
'''

numbers = list(range(10)) #range crée une liste séquentielle de chiffres
print(numbers)
>>>[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers = list(range(3, 8)) #range les chiffres entre 3 et 8 (2 args)
print(numbers)

range(20) == range(0, 20)

numbers = list(range(5, 20, 2)) #range peut avoir un 3eme arg, qui détermine l'intervalle de la séquence
print(numbers)
>>>

#FONCTIONS
def ma_fonc(): #def créé une fonction
  print("spam")
  print("spam")
  print("spam")
#Les fonctions doivent être créés avant de pouvoir être appelées (comme les variables)
ma_fonc() #Appelle la fonction

def print_avec_exclamation(word): #Les fonctions peuvent prendre des arguments
   print(word + "!")

#Des fonctions avec un nom court sont préférables, ce nom est un très mauvais exemple
print_avec_exclamation("spam") #La valeur donnée prend la place de la variable word de la fonction
print_avec_exclamation("eggs")
print_avec_exclamation("python")

excla = print_avec_exclamation #Les foncs peuvent être assignées à une variable comme tout autre objet
print(excla("meme"))

def somme_deux_fois(x, y): #Elles peuvent prendre plusieurs arguments
   print(x + y)
   print(x + y)

somme_deux_fois(5, 8) #Ici, 5=x et 8=y, à cause de leur position


def max(x, y): 
    if x >=y:
        return x  #Si la valeur du if est True, max renvoie la valeur x
    else:
        return y  #return met fin à la fonction, tout code présent aprèssera ignoré
        print("Je ne serais jamais éxecuté")
        
print(max(4, 7))
z = max(8, 5)
print(z)


def add(x, y=0): #On peut assigner une valeur par défaut à une variable, qui sera utilisée si
  return x + y   #aucune valeur n'est donnée lors de l'appel, dans le cas contraire on utilise celle de l'appel
print(add(1)) #1+0
>>>1

def deux_fois(func, x, y): #Une fonc peut être utilisée comme arg
  return func(func(x, y), func(x, y))

a = 5
b = 10

print(deux_fois(add, a, b)) #Les foncs peuvent aussi être utilisées en tant qu'arguments

value = random.randint(1, 6) #Ceci est un appel à la fonction randint du module random, importé tout en haut

#!!!!!! METTRE LES TRUCS AVEC LES ARGUMENTS OPTIONNELS

#EXCEPTIONS
try:  #Tente d'éxécuter le code
   num1 = 7
   num2 = 0
   print (num1 / num2)
   print("Calcul terminé")

#Si une erreur survient lors de l'éxecution, les blocks except vont s'éxecuter
except ZeroDivisionError: #Si l'erreur est une erreur de type ZeroDivisionError (div par 0), se block s'éxécute
   print("Une erreur est survenue\nCause: Division par zéro")
   except (ValueError, TypeError): #On peut utiliser un même block pour plusieurstypes d'erreurs
   print("Une erreur de valeur ou de type est survenue") #And have mutliple errors to handle
  except:         #Un block except sans arg s'occupe de toutes les erreurs (ou celles qui ne sont pas égales aux blocks précédents)
   print("Une erreur est survenue")
finally:  #Un block qui s'éxecute peu importe si il y a eu une erreur ou non
   print("Ce code va s'éxecuter peu importe ce qui se passe avant")
   raise ValueError("ceci est un test") #Ceci déclenche une erreur de type ValueError
   #On peut donner des infos sur l'exception en les mettant en arguments

   try:
   num = 5 / 0
except:
   print("Une erreur est survenue")
   raise #Raise sans arg va re-déclencher la dernière erreur qui s'est produite
>>>Une erreur est survenue
ZeroDivisionError: division by zero


#FICHIERS
fichier = open("filename.txt") #On ouvre un fichier en vue de le lire ou l'éditer

'''
On peut spécifier le mode d'ouverture d'un fichier en ajoutant un second argument à la fonction open()
"r" = read mode; mode lecture. C'est le mode par défaut. 
"w" = write mode; mode écriture. Supprime tout le contenu d'un fichier pour réecrire dessus.
"a" = append mode; mode ajout. Ajoute le texte donné après les données existantes.

Ajouter "b" à un mode (rb, wb) ouvre le fichier en mode binaire,
utile pour les fichier non texte (comme les images and fichiers son).
'''
fichier2 = open("afile.txt", "w")
# Manipulations avec le fichier
fichier2.close() #Lorsqu'on en a fini avec le fichier, on doit le fermer

fichier = open("filename.txt", "r") #Lire des fichiers
cont = file.read() #Cont == le contenu entier du fichier
print(cont)
fichier.close()

fichier = open("filename.txt", "r")
print(fichier.read(16)) #WOn peut passer le nombre d'octets du fichier qu'on souhaite lire
print(fichier.read(4)) #+ d'appels = + du fichier lu tranche d'octets par tranche d'octets
print(fichier.read(4))
print(fichier.read()) #Print le reste du fichier
fichier.close()  #Si on tente de lire le fichier après avoir atteint la fin, on a une string vide

autrefichier = open("newfile.txt", "w") #Le mode "w" crée un nouveau fichier si il n'existe pas
autrefichier.write("This has been written to a file") #On écrit dans le fichier
autrefichier.close()

#Quand on ouvre un fichier en mode write, tout le contenu existant précédemment est supprimé

'''
Il est de bonne mesure de fermer le fichier après qu'on ai fini de l'utiliser.
Une bonne façon de faire cela est d'utiliser try et finally.
Cela nous assure que le fichier sera fermé, même si une erreur survient.
'''
try:
   f = open("filename.txt")
   print(f.read())
finally:
   f.close()
'''
Une autre façon de le faire est d'utiliser des boucles with
Cela crééra une variable temporaire (souvnet appellée "f")
qui est accessible seulement a l'intérieur de la boucle.

Le fichier est automatiquement fermé à la fin de la boucle,
même si des exceptions surviennent.
'''
with open("filename.txt") as f:
  print(f.read())

#L'objet None est le même que dans d'autres languages, il représente un objet nul.

#TUPLES

