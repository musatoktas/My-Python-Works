Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x =12
>>> if x<11 :
	print("Bayagi kucuk bi rakam secmissiniz")
elif x=12:
	
SyntaxError: invalid syntax
>>> if x<11 :
	print("Bayagi kucuk bi rakam secmissiniz")
elif x==12:
	print(" tam onikiden vurdunuz")
else x>12:
	
SyntaxError: invalid syntax
>>> if x<11 :
	print("Bayagi kucuk bi rakam secmissiniz")
elif x==12:
	print(" tam onikiden vurdunuz")
else x>>12:
	
SyntaxError: invalid syntax
>>> x=12
>>> if x<11 :
	print("Bayagi kucuk bi rakam secmissiniz")
elif x=12:
	
SyntaxError: invalid syntax
>>> x =12
>>> if x<11 :
	print("Bayagi kucuk bi rakam secmissiniz")
elif x==12:
	print(" tam onikiden vurdunuz")
else x>12:
	
SyntaxError: invalid syntax
>>> if x<11 :
	print("Bayagi kucuk bi rakam secmissiniz")
elif x==12:
	print(" tam onikiden vurdunuz")
else :
	print("X biraz buyuk olmus" )

	
 tam onikiden vurdunuz
>>> cast = ["Al Pacino", "Marlon Brando", "Jason Statham", "Bruce Wills"]
>>> for i in cast:
	print(i)

	
Al Pacino
Marlon Brando
Jason Statham
Bruce Wills
>>> for c in cast:
	print(c)
	print(len(c))

	
Al Pacino
9
Marlon Brando
13
Jason Statham
13
Bruce Wills
11
>>> for x in range(10):
	print(x)

	
0
1
2
3
4
5
6
7
8
9
>>> for x in range(10, 19, 2):
	print(x)

	
10
12
14
16
18
>>> buttcrack = 5
>>> while buttrcrack <10:
	print(buttcrack)
	buttcrack +=2

	
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    while buttrcrack <10:
NameError: name 'buttrcrack' is not defined
>>> while buttcrack <10:
	print(buttcrack)
	buttcrack +=2

	
5
7
9
>>> ucak = 19
>>> while ucak >12:
	print("12 19 dan kcuk")
	ucak += 2
