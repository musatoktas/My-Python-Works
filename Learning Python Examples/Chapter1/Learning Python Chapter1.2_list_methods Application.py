Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Today I will applicate lit methods. I choose this form Enes KEmal Ergin LEarning Pythin REpository. Chapter1.2_list_methods
>>> #first we will determinate aist
>>> #first we will determinate a list
>>> cast =["Elma","Armut","Ananas","Kiwi"]
>>> print(cast) #show the list
['Elma', 'Armut', 'Ananas', 'Kiwi']
>>> #may be you wantto show specific member of the list
>>> print(cast[1])
Armut
>>> print(cast[4])
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(cast[4])
IndexError: list index out of range
>>> print(cast[0])
Elma
>>> print(cast[-1])
Kiwi
>>> # "append()" function add a new member in to the list. But you can add just 1 element
>>> cast.append("muz")
>>> print(cast)
['Elma', 'Armut', 'Ananas', 'Kiwi', 'muz']
>>> # Also you can delete the last member by "cast.pop()" function
>>> cast.pop
<built-in method pop of list object at 0x03050418>
>>> print(cast)
['Elma', 'Armut', 'Ananas', 'Kiwi', 'muz']
>>> cast.pop(2)
'Ananas'
>>> print(cast)
['Elma', 'Armut', 'Kiwi', 'muz']
>>> #now you can see we can delete which one you want.
>>> cast.pop(1,3)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    cast.pop(1,3)
TypeError: pop() takes at most 1 argument (2 given)
>>> #extend() function is work for add more than 1
>>> cast.extend(["Lahana","KArniyarik","Dolma])
	     
SyntaxError: EOL while scanning string literal
>>> cast.extend(["Lahana","KArniyarik","Dolma"])
>>> print(cast)
['Elma', 'Armut', 'Kiwi', 'muz', 'Lahana', 'KArniyarik', 'Dolma']
>>> # "cast.remove("name")"its work for delete specific elment. You can delete by write member of the list name where write name in the function.
>>> cast.remove("LAhana")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    cast.remove("LAhana")
ValueError: list.remove(x): x not in list
>>> cast.remove("Lahana")
>>> print(cast)
['Elma', 'Armut', 'Kiwi', 'muz', 'KArniyarik', 'Dolma']
>>> # now we cannot see "Lahana", in the list.
>>> #The last function is work for adds an element in the specific location.
>>> cast.insert(2,"Sogan")
>>> print(cast)
['Elma', 'Armut', 'Sogan', 'Kiwi', 'muz', 'KArniyarik', 'Dolma']
>>> 
