# ------------------------------------------------------------------
# Variables and Strings

sarah, bob, mike = 16, 21, 17
name, age = "Maurice", 30
print(name, age)

print("He"*3)   # Repeats the string multiple times


sent1 = "Today is Friday"
print(sent1 , name)  # Places a space between arguments
print(sent1 + name)  # No space between strings

#String indexes start from 0 as in C
print(name[0])      # Print first character
print(name[3:5])    # Print 4th to 5th position. Last character is NOT included!
print(name[:3])     # Print first 3 characters
print(name[:-2])    # Print all characters except last two
  

#  % Symbol - For substituting
message = "%s is 15 years old"
print(message%"Avi")      # Prints Avi is 15 years old

message2 = "%s %s is POTUS"
print(message2%("Barrack","Obama"))  # Prints Barrack Obama is POTUS

message3 = "%s is %d years old"
print(message3%("Obama",50))         # Prints Obama is 50 years old   


# -------------------------------------------------------------------
# Lists []
#
shopList = [ 'Apples', 'Oranges', 'Bananas', 'Cheese']
print( shopList[2] )  # Prints Bananas
print( shopList[0:2]) # Prints Apples Oranges   (last indes is NOT included!)    ['Apples', 'Oranges']  

shopList.append("Blueberies")  # Add new item [ 'Apples', 'Oranges', 'Bananas', 'Cheese', 'Blueberries']
shopList[0] = "Cherries"       # Update existing item [ 'Cherries', 'Oranges', 'Bananas', 'Cheese', 'Blueberries']
del shopList[1]                # Delete item  [ 'Cherries', 'Bananas', 'Cheese', 'Blueberries']

print("Lenght of the list :" , len(shopList))           # len() return how many items are the in the list

listNum = [1,4,7,23,6]
print( "listNum is ", listNum )
print( "Maximum value of listNum %d   Minimum value of listNum %d"%(max(listNum), min(listNum)) )


# ---------------------------------------------------------------------
# Dictionary {}
#  Key - Value pairs
#
students = {"Bob":12, "Rachel":13, "Emily":15}    # Bob is the key, 12 is the value
print(students)     # We get:   {'Emily':15, 'Bob':12, 'Rachel':13}

print("Age of Rachel is " , students["Rachel"] )   # Get a the value for a key
students["Rachel"]=14           # Update the value for given key
print("New Age of Rachel is " , students["Rachel"] )   # Get a the value for a key

del students["Emily"]   # Remove item from dictionary with the key


# ----------------------------------------------------------------------
# Tuples (tupıl)   ()
# Just like lists, but Tuples can't be changed. 
#
tup = ( 'oranges', 'apples', 'bananas' )
# tup[0] = 'cherries'    # This is INVALID! Values can't be changed, removed, updated

print(tup[0:2])   # prints ('oranges', 'apples')   Last index is NOT included

tup2 = (12, 14)
tup3 = tup + tup2    # this is valid. we can append tuples
print(tup3)      # prints ('oranges', 'apples', 'bananas', 12, 14)

# ----------------------------------------------------------------------
# statements
#  >  <    >=   <=  ==  !=   
# and  or
if ( 5 > 3 ):
    print("Hello")        # not going to print this

if ( 3 < 2 ):
    print("not going to print this")
else:
    print("going to print this")

# Comparison  is  "==" like C
print ( 3== 2 )           # prints   false
print ( 3== 3 )           # prints   true

age = 16
if ( age < 13 ):
    print("You are young")
elif ( age >= 13 and age < 18 ):         # Do not forget the ":"
    print("You are a teenager")
else:
    print("You are an adult")

# ------------------------------------------------------------------------
# for loops
#
list1 = ["Apples", "Bananas", "Cherries"]
tup1 = (13,12,15)

print("Iterating over list1 : ")
for iterating_item in list1:
    print(iterating_item)

print("Iterating over tup1 : ")
for iterating_item_tup in tup1:
    print(iterating_item_tup)

print("Range function for for loops for iteration : ")
for i in range(0,4):       # range function does NOT include LAST index
    print(i)        # Prints  0 to 3  

#for x in len(name):
#  print(name[x])

for i in range(0,11,2):   # 2 is the skip value or increment factor
    print(i)       # prints  0 2 4 6 8 10      (not in the same line)

print("2d iteration")
for i in range(0,3):
    for j in range(0,2):
        print(i*j)

# --------------------------------------------------------------------------
# while loops
#
print("While function:")
c = 0
while c < 5:                  # prints 0 1 2 3 4    (not in the same line)
    print( c )
    c = c + 1                  

print("while-break:")
c = 0
while c < 5:                  # prints 0 1 2 3      (not in the same line)
    print(c)
    if c == 3:
        break
    c = c + 1

print("while-continue:")
c = 0
while c < 5:                  # prints 1 2 4 5      (not in the same line)
    c = c + 1
    if c == 3:
        continue
    print(c)

print("while-pass:")
c = 0
while c < 5:
    c = c + 1
    if c == 3:
        pass      # fill... null function.. like nop... mostly for TODO
    print (c)


# --------------------------------------------------------------------------
# try - except
#

try: 
    if name > 3:
        print("Hello")
except: 
    print("There is something wrong with your code. name is not defined")


"""
This is a multiple line
comment for you
"""
