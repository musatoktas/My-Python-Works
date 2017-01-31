Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> my_list = ("Hello World")
>>> my_list
'Hello World'
>>> my_list = list("Hello World")
>>> 
>>> 
>>> my_list
['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
>>> x= []
>>> x
[]
>>> x = ("as")
>>> x
'as'
>>> x= ["as"]
>>> 
>>> x
['as']
>>> 
>>> x= [1,2,3,4]
>>> x
[1, 2, 3, 4]
>>> x[1] = "string"
>>> x
[1, 'string', 3, 4]
>>> del x[2]
>>> x
[1, 'string', 4]
>>> name = list("Perl")
>>> name
['P', 'e', 'r', 'l']
>>> name[2:] = list("ar")
>>> 
>>> name
['P', 'e', 'a', 'r']
>>> #its pretty cool thing which I wrote, for change the part of the list.
>>> x
[1, 'string', 4]
>>> x.append(a)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    x.append(a)
NameError: name 'a' is not defined
>>> x.append(3)
>>> x
[1, 'string', 4, 3]
>>> x = [[1,2],1,2,3, [2,1,[1,2]]]
>>> x
[[1, 2], 1, 2, 3, [2, 1, [1, 2]]]
>>> #how many member in the list?
>>> x.count(1)
1
>>> # okay it doesnt work..
>>> lst= [123,654,2345,12143234]
>>> len(lst)
4
>>> #okay we got it now, what we want)
>>> max(lst)
12143234
>>> min(lst)
123
>>> sum(lst)
12146356
>>> sorted(lst)
[123, 654, 2345, 12143234]

>>> a =[1,2,3]
>>> b = [4,5,6]
>>> print (a+b)
[1, 2, 3, 4, 5, 6]
>>> a
[1, 2, 3]
>>> #how can we gettogether list and b?
>>> a.extend(b)
>>> a
[1, 2, 3, 4, 5, 6]
>>> #now you can see we get them together under the list a
