
# inserting new line by \n between words (escape sequence)
print('hello \n world')
print('hello \nworld')


# inserting tab space by \t between lines (escape sequence)
print('hello \t world')
print('hello \tworld')


# length funcion bye len (includes spaces too)
len('hello')
len('he is')


# indexing by square brackets (starts with 0 and space counts)
string = "hello"
string[3]
string[1]


# reverse indexing (starts with zero and ends in descending order with -1 at last )
string = "hello"
string[0]
string[-4]
string[-1]


# ------------------------- slicing [start:stop:step] 
# stop index does not include the that index position
string = "abcdefghijk"
string[4:] # from 4 to end
string[:4] # from begining to 4
string[2:5] # from 2 to 5
string[::] # from begining to end

#stepping is used to jump
string[::3] # skips 2 positions in this case
string[1:10:2] # skips 1 position from 1 to 10
string[::-1] # reverses the string


# --------------------Immutability and Concatenation
# strings are immutable (can't change/mutate)

# changing "stream" to "dream" by Concatenation (joining strings)
word = "steam"
last_letters = word[2:] # test "last_letters" string now (eam)
"dr" + last_letters # we joined dr with eam

x = "hello"
y = ", how are you?"
x + y # 'hello, how are you?'

# Concatenation by mulitplying
letter = "z"
letter * 9

# strings with numbers don't sum up by Concatenation
x = "2"
y = "3"
x + y # '23'


# ------------------- built-in string methods (calling)
# functions inside the object (used with a dot '.')
x = 'Hello World'
x.upper() # 'HELLO WORLD'
x = x.upper() # makes the original x go upper case

# split method splits string into a list based on the whitespace
x = "this is an example of splitting"
x.split() # ['this', 'is', 'an', 'example', 'of', 'splitting']
x.split('i') # splits the string from letter 'i'


# ---------------------- string Interpolation
# injecting a variable into string for printing by plus sign '+'
# .format() method - inserts the strings supplied into the curly braces)
print("This is a string {}".format('INSERTED'))
print('{}{}'.format('Hello',' World'))
print("{1} {0}".format('Hello','World')) # inserting the strings based on the index position
print("{0} {0}".format('Hello','World'))
print("{h} {w}".format(h = 'Hello', w = 'World')) # assigning variables to the string

# float formatting with .format() method {value:width.precision f}
result = 22/7
print("I got {r:1.2f} out of pi".format(r = result)) # width denotes whitespace and value before f denotes decimal place
    
# formating strings literals (F strings)
# placing 'f' before what to be printed and writing string variable directly into curly braces
name = "Himank"
print(f"Hello, my name is {name}.")

# assigning multiple variables via F strings 
h = "How"
a = "are"
y = 'you'
print(f"{h} {a} {y}") # "How are you"


# ------------------------------ Lists
# lists contain variety of objects like str, int, float and is seperated by commas in square brackets
mylist = ["string", 1, 1.0]
type(mylist) # = "list"
len(mylist) # "3"

# indexing in list
mylist = ['one', 'two', 'three']
mylist[0]
mylist [2]

# slicing in list
mylist = [1,2,3,4,5,6,7,8,9]
mylist[3:7] # [4, 5, 6, 7]
mylist [2:9:2] # [3, 5, 7, 9]

# Concatenation in list
mylist = [1,2,3,4,5]
anotherlist = [6,7,8,9]
newlist = mylist + anotherlist # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# lists are mutable (they can be changed unlike strings)
mylist = [1,2,3] 
mylist[0] = "ONE IN CAPS"
mylist # ['ONE IN CAPS', 2, 3]

# adding new item at the end of the list by .append() function
mylist = [1,2,3,4]
mylist.append(5)
mylist # [1, 2, 3, 4, 5]

# inserting new object on a particular index/position by .insert() function 
mylist = [1,2,3,4,5]
mylist.insert(6, 6) # .insert(index, object)
mylist # [1, 2, 3, 4, 5, 6]

# removing item from end of the list by .pop()function
mylist = [1,2,3,4]
mylist.pop()
mylist # [1, 2, 3]

#removing an object by .remove() function
mylist = [1,2,3,4,5,6]
mylist.remove(5)
mylist # [1, 2, 3, 4, 6]


# ------------------------------- Dictionary
# unordered mapping for storing objects using key:value pairs in curly braces
mydict = {'key1':'value1','2':'value2'} 
mydict['key1'] # 'value1'

mydict = {'apple':20, 'grapes':15, 'orange':25}
mydict['grapes'] # 15
mydict['apple'] # 20

# dictionary can also store lists and another dictionary inside it
mydict = {'a':2, 'b':3.5, 'c':'string', 'd':['this','is','list'],'e':{'another':'dictionary'}}

mydict['d'][0] # 'this'
mydict['d'][1]# 'is'

mydict['d'] # ['this', 'is', 'list']
mydict['e'] # {'another': 'dictionary'}
mydict['e']['another'] # 'dictionary'

# using functions in dictionaries with different objects (stack calls)
mydict['d'][1].upper() # 'IS'
mydict['e']['another'].upper() # 'DICTIONARY'

# adding new key-value pair to dictionary
mydict = {'int':12, 'str':'string'}
mydict['float'] = 10.0
mydict # {'int': 12, 'str': 'string', 'float': 10.0}

# overwriting key-value pair
mydicit = {'int':10, 'float':'string'}
mydict['int'] = 20
mydict['int'] # 20

# functions in dictionaries (calling)
mydict = {'apple':20, 'grapes':15, 'orange':25}
mydict.keys() # dict_keys(['apple', 'grapes', 'orange'])
mydict.values() # dict_values([20, 15, 25])
mydict.items() # dict_items([('apple', 20), ('grapes', 15), ('orange', 25)])


# ------------------------------- Tuples
# tuples are like list but the're immutable (can;t change) and they use paranthesis
t = (1,2,3)
type(t) # tuple
len(t) # 3

# inbuilt functions with tuples
t = (1,1,2,3,3,3,4,4)
t.count(1) # 2
t.count(3) # 3

t.index(2) # 2 (where it first appears)
t.index(4) # 6

# mutability
l = [1,2,3]
l[0] = 'ONE'
l[0] # 'ONE'

t = (1,2,3)
t[0] = 'ONE' # 'tuple' object does not support item assignment


# ---------------------------------- Sets
# unordered collection of unique elements (no repetation)

myset = set()
myset # set()
myset.add(1)
myset # {1}
myset.add(2)
myset # {1, 2}

mylist = [1,1,2,3,3,3,4,4,4,4,5]
set(mylist) # {1, 2, 3, 4, 5}


# ----------------------------- Booleans
# True/False
type(True) # bool

1 < 2 # True
1 == 1 # True

    


















