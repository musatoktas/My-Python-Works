Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> name = "Canavar Cafer"
>>> print(name[1])
a
>>> name[3]
'a'
>>> name[3:6]
'ava'
>>> name[:]
'Canavar Cafer'
>>> print('eqwe')
eqwe
>>> len('asdasdasdasda')
13
>>> # "len()" code is count the how many character in the strings.
>>> len(name)
13
>>> #I want to talk again about list
>>> numbers = [23,12,51,43]
>>> numbers[3]
43
>>> numbers + [123,54,23,74,98]
[23, 12, 51, 43, 123, 54, 23, 74, 98]
>>> numbers
[23, 12, 51, 43]
>>> #youcan see when you add new list after first list you can not change orginal
>>> """ youcan see when you add new list after first list you can not change orginal list. if you want add a new list after numbers list or your list  {I dont know what is your list name :D} you can use ".append(x)" code. you have t write your new member where x place."""
' youcan see when you add new list after first list you can not change orginal list. if you want add a new list after numbers list or your list  {I dont know what is your list name :D} you can use ".append(x)" code. you have t write your new member where x place.'
>>> numbers[0:2]
[23, 12]
>>> numbers[:2]
[23, 12]
>>> numbers.append(102,12)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    numbers.append(102,12)
TypeError: append() takes exactly one argument (2 given)
>>> # it says you can add only one member in to the list by this [.append()] code
>>> numbers.append(102)
>>> numbers
[23, 12, 51, 43, 102]
>>> # we can use .extend() for add list behind to our list
>>> numbers.extend()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    numbers.extend()
TypeError: extend() takes exactly one argument (0 given)
>>> numbers.extend([120, 123, 34, 54])
>>> numbers
[23, 12, 51, 43, 102, 120, 123, 34, 54]
>>> #now you can see what I mean
>>> #you can change members of the list like this
>>> numbers[4:6] = [67]
>>> numbers
[23, 12, 51, 43, 67, 123, 34, 54]
>>> #if you inspect carefully you can see 6th element 102 changed to 67.
>>> #Also You can remove or change a part of the list members. Let me show you that
>>> numbers[2:5] = [11, 12 ,13 , 14]
>>> numbers
[23, 12, 11, 12, 13, 14, 123, 34, 54]
>>> numbers[:5] = []
>>> numbers
[14, 123, 34, 54]
>>> 
