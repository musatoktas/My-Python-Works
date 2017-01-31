Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> True or False
True
>>> True and False
False
>>> #These are fundamentals of the basic logic, and I want to remind these also membersw of the boolean.
>>> #Now let's understand While loop.
>>> x = 1
>>> x += 1
>>> x
2
>>> x+= 1
 
>>> x
3
>>> while n>10:
	print(n)
	n-= 1

	
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    while n>10:
NameError: name 'n' is not defined
>>> # This problem cause is we didn't determinate n variable. So now this problem is should be solve.
>>> n=39
>>> while n>10:
	print(n)
	n-=2

	
39
37
35
33
31
29
27
25
23
21
19
17
15
13
11
>>> n=39
>>> while True:
	line = input(">")
	if line == "done":
		break
	print(line)

	
>as
as
>d
d
>asd
asd
>as
as
>das
das
>d
d
>asd
asd
>sa
sa
>done yazarsak bitecek
done yazarsak bitecek
>done
>>> while True:
	print ("Welcome", i, "times. To stop press[CTRL+C]")
	i +=1
	time.sleep(2) #It just delays for 2 second

	
Traceback (most recent call last):
  File "<pyshell#30>", line 2, in <module>
    print ("Welcome", i, "times. To stop press[CTRL+C]")
NameError: name 'i' is not defined
>>> import time
>>> i=1
>>> while True:
	print("Welcone", i, "times. To stop press [CTRL+C]")
	i += 1
	time.sleep(2) #It just delays for 2 second

	
Welcone 1 times. To stop press [CTRL+C]
Welcone 2 times. To stop press [CTRL+C]
Welcone 3 times. To stop press [CTRL+C]
Welcone 4 times. To stop press [CTRL+C]
Welcone 5 times. To stop press [CTRL+C]
Welcone 6 times. To stop press [CTRL+C]
Welcone 7 times. To stop press [CTRL+C]
Welcone 8 times. To stop press [CTRL+C]
Welcone 9 times. To stop press [CTRL+C]
Welcone 10 times. To stop press [CTRL+C]
Welcone 11 times. To stop press [CTRL+C]
Welcone 12 times. To stop press [CTRL+C]
Welcone 13 times. To stop press [CTRL+C]
Welcone 14 times. To stop press [CTRL+C]
Welcone 15 times. To stop press [CTRL+C]
Welcone 16 times. To stop press [CTRL+C]
Welcone 17 times. To stop press [CTRL+C]
Welcone 18 times. To stop press [CTRL+C]
Welcone 19 times. To stop press [CTRL+C]
Welcone 20 times. To stop press [CTRL+C]
Traceback (most recent call last):
  File "<pyshell#38>", line 4, in <module>
    time.sleep(2) #It just delays for 2 second
KeyboardInterrupt
>>> while True:
	line = input(">")
	if line[0] == "#":
		continue
	if line == "done":
		break
	print(line)

	
>
Traceback (most recent call last):
  File "<pyshell#46>", line 3, in <module>
    if line[0] == "#":
IndexError: string index out of range
>>> while True:
	line = input(">")
	if line[0] == "#":
		continue
	if line == "done":
		break
	print(line)

	
>
Traceback (most recent call last):
  File "<pyshell#48>", line 3, in <module>
    if line[0] == "#":
IndexError: string index out of range
>>> 
KeyboardInterrupt
>>> while True:
	line = input(">")
	if line[0] == "#":
		continue
	if line == "done":
		break
	print(line)

	
>\
\
>\
\
>2132
2132
>32
32
>3
3
2>3
3
>23
23
>23
23
>23
23
>23
23
>23
23
>2
2
>
Traceback (most recent call last):
  File "<pyshell#50>", line 3, in <module>
    if line[0] == "#":
IndexError: string index out of range
>>> 
>>> #After these examples I think 90% of students can be understand mission of the while loop.
>>> #now we will look another thing
>>> for i in "Python":
	print(i, end = "-")

	
P-y-t-h-o-n-
>>> # also
>>> for i in "python"
SyntaxError: invalid syntax
>>> for i in "Python":
	print(i)

	
P
y
t
h
o
n
>>> for i in "Python"
SyntaxError: invalid syntax
>>> for i in "Python":
	print(i,i)

	
P P
y y
t t
h h
o o
n n
>>> for k in "Python":
	print(k,i)

	
P n
y n
t n
h n
o n
n n
>>> k
'n'
>>> i
'n'
>>> p
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    p
NameError: name 'p' is not defined
>>> #there were some expantions for see the python consequences.
>>> 
>>> 
