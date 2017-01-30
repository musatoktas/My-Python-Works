

    print "Welcome My Python Notes"
    #Hash mark is comment tag for python
    """ for multiple line comment dont be afraid to use triple quotation mark!"""

###Boolean  Syntax

    a = True
    b= False

Its the simplest language I ever seen before!

###Basic Math

You are eligible to do addition substraction multiplication and division on the Python.

Exmp: 

    a= 56988+9656
    printf a
    eight= 2**8
    printf eight
  108%100 is equal to reminder of the division
Note that I use '**' instead of  one of it because that mean s 3 power of 2. You can combine different variables in python so thats the other cool thing for me.
 

    <h3>String's</h3>

Another useful data type is the string. A string can contain letters, numbers, and symbols. You also can assign different strings to other strings.

    <h5>-Escaping characters-</h5>

There are some characters that cause problems. For example:

    'There's a snake in my boot!'

This code breaks because Python thinks the apostrophe in 'There's' ends the string. We can use the backslash to fix the problem, like this:

    'There\'s a snake in my boot!'

<h4>String methods</h4>
Great work! Now that we know how to store strings, let's see how we can change them using string methods.

String methods let you perform specific tasks for strings.

We'll focus on four string methods:

    len()
    lower()
    upper()
    str()

Let's start with `len()`, which gets the length (the number of characters) of a string!

    .upper() and .lower() only work in strings

`str(#)=` is using for adding some kind of variables between the strings 
String Formatting with `%`, Part 1
When you want to print a variable with a string, there is a better method than concatenating strings together.

    name = "Mike"
    print "Hello %s" % (name)

The `%` operator after a string is used to combine a string with variables. The `%` operator will replace a `%`s in the string with the string variable that comes after it.

<h2> Short Review about the String's Methods</h2>
Great job! You've learned a lot in this unit, including:

Three ways to create strings

    'Alpha'
    "Bravo"
    str(3)

String methods

    len("Charlie")
    "Delta".upper()
    "Echo".lower()

Printing a string

    print "Foxtrot"

Advanced printing techniques

    g = "Golf"
    h = "Hotel"
    print "%s, %s" % (g, h)

<h3>Date-Time Printing Codes</h3>

    from datetime import datetime
    now = datetime.now()
    
    print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year,now.hour, now.minute, now.second,)

<h3>Comparators</h3>

 1. Equal to (==) 
 2. Not equal to (!=) 
 3. Less than (<) 
 4. Less than or equal to  (<=) 
 5. Greater than (>) 

<h3>Detailed Boolean Operators</h3>

    """
      Boolean Operators
         
  True and True is True
  True and False is False
    False and True is False
    False and False is False
    
    True or True is True
    True or False is True
    False or True is True
    False or False is False
    
    Not True is False
    Not False is True
    
    """
    
   Advance Boolean Priorties

 1. not is evaluated first; 
 2. and is evaluated next; 
 3. or is evaluated last.

Set `bool_one` equal to the result of `False` or not `True` and `True`
Set `bool_two` equal to the result of `False` and not True or True
Set `bool_three` equal to the result of `True` and not (`False` or `False`)
Set `bool_four` equal to the result of not not `True` or `False` and not `True`
Set `bool_five` equal to the result of `False` or not (`True` and `True`)


    bool_one = False
    
    bool_two = True
    
    bool_three = True
    
    bool_four = True
    
    bool_five = False

The Big If
Really great work! Here's what you've learned in this unit:

Comparators

    3 < 4
    5 >= 5
    10 == 10
    12 != 13

Boolean operators

  True or False 

    (3 < 4) and (5 >= 5)
    this() and not that()

Conditional statements

    if this_might_be_true():
        print "This really is true."
    elif that_might_be_true():
        print "That is true."
    else:
        print "None of the above."

Let's get to the grand

<h3>Get Input from User</h3>

    name = raw_input("What's your name?")
    print name

In the above example, `raw_input()` accepts a string, prints it, and then waits for the user to type something and press Enter (or Return).

<h4>Go All the Way End </h4>
When slicing until the end of the string, instead of providing `len(new_word)`, you can also not supply the second index:

<h2>Functions</h2>

----------

`def` is working for defining new functions. Functions are reusable piecce of codes.

<h4>Function Junction</h4>
Functions are defined with three components:

The header, which includes the def keyword, the name of the function, and any parameters the function requires. Here's an example:

    def hello_world(): // There are no parameters

An optional comment that explains what the function does.

    """Prints 'Hello World!' to the console."""

The body, which describes the procedures the function carries out. The body is indented, just like for conditional statements.

    print "Hello World!"

Here's the full function pieced together:

    def hello_world():
        """Prints 'Hello World!' to the console."""
        print "Hello World!"
**Tip**  You can call the functions by using nothing here is an example;

    square(n) 
as you can see here there is no additional code require to call the functions.

**Tip** Importing modules;

  import math
    print math.sqrt(25)

We import math module because calculate the squareroot of 25. Instead of typing every time long "`math.sqrt()`" you can import this code completely and you can use it like "`sqrt()`" mode. Here is the way of this;

    from module import function

(do not type paranthesees.)

You can aso import all codes from the module by using "*" sign

    from module import *
Universal imports may look great on the surface, but they're not a good idea for one very important reason: they fill your program with a ton of variable and function names without the safety of those names still being associated with the module(s) they came from.

**Tip** To checkout whats in the module you can follow these steps;

    import math            # Imports the math module
    everything = dir(math) # Sets everything to a list of things from math
    print everything       # Prints 'em
<h4>Not require to import modules functions</h4>

 `max ()` Function
  This function is detect what is the maximum of # the list. That # can be integer or float.
  `min()` Function
 It is absoultely conversion of `max()` function.
 `abs()` function
The `abs()` function returns the absolute value of the number it takes as an argument—that is, that number's distance from `0` on an imagined number line. For instance, `3` and `-3` both have the same absolute value: `3`. The `abs()` function always returns a positive value, and unlike `max()` and `min()`, it only takes a single number.

`type()` Function
Finally, the `type()` function returns the type of the data it receives as an argument. If you ask Python to do the following:

    print type(42)
    print type(4.2)
    print type('spam')

Python will output:

    <type 'int'>
    <type 'float'>
    <type 'str'>
<h4>The Last Exampleof the Function</h4>

    def shut_down(s):
        if s == "yes":
            return "Shutting down"
    
        elif s == "no":
            return "Shutdown aborted"
    
        else:
            return "Sorry"
<h2>Lists</h2>
----------

    letters[1, "sadf", 5]
    letters.append("a")//Addition to the list
    letters[1:#]//cutting a slice from list
example of sliceing codes:

    suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]
    
    first  = suitcase[0:2]  # The first and second items (index zero and one)
    middle = suitcase[2:4] # Third and fourth items (index two and three)
    last   = suitcase[4:6]  # The last two items (index four and five)

<h4>Filling lists with the For Loop</h4>
  
    start_list = [5, 3, 1, 2, 4]
    square_list = []
    
    for n in start_list:# Your code here!
        square = n ** 2
        square_list.append(square)
        square_list.sort()
    
    print square_list

<h3>Dictionary and List Codes</h3>

    inventory['pocket'] = ['seashell', 'strange berry', 'lint']
    inventory['backpack'].remove('dagger')
    inventory['backpack'].sort()
<h4>Again `for` loop</h4>

    a = ["List of some sort”]
    for x in a: 
        # Do something for every x


----------


    
    for item in [1, 3, 21]: 
            print item


----------

    # A simple dictionary
    d = {"food" : "bar"}
    
    for key in d: 
        print d[key]  # prints "bar" 
            


----------
this code printing even numbers in the `a` list
   
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    
    for number in a:
        if number % 2 == 0:
            print number


----------

Owning a supermarket (Dictionary Applications)
Instructions

 1. Define a function `compute_bill` that takes one argument `food` as
    input. 
    
 2. In the function, create a variable `total` with an initial
    value of zero. 
    
 3. For each item in the food list, add the `price` of that
    item to `total`. 
 4. Finally, return the `total`. Ignore whether or not the
    item you're billing for is in stock.

Note that your function should work for any food list.
shopping_list = ["banana", "orange", "apple"]

    stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
    }
        
    prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }
    
    # Write your code below!
    def compute_bill(food):
        total = 0
        for i in food:
            if stock[i] > 0:
                total = total + prices[i]
                stock[i] = stock[i] - 1
        return total


----------


Ending up with Dictionaries with this last syntax example below;

    lloyd = {
        "name": "Lloyd",
        "homework": [90.0, 97.0, 75.0, 92.0],#there is no indent bw colon and Quot mark
        "quizzes": [88.0, 40.0, 94.0],#it must be single quote not double
        "tests": [75.0, 90.0]
    }
    alice = {
        "name": "Alice",
        "homework": [100.0, 92.0, 98.0, 100.0],
        "quizzes": [82.0, 83.0, 91.0],
        "tests": [89.0, 97.0]
    }
    tyler = {
        "name": "Tyler",
        "homework": [0.0, 87.0, 75.0, 22.0],
        "quizzes": [0.0, 75.0, 78.0],
        "tests": [100.0, 100.0]
    }

----------
<h3>Using `for` Loop Effectively (IMPORTANT!)</h3>

    students = [lloyd, alice, tyler]
    
    for student in students:
        print student['name']
        print student['homework']
        print student['quizzes']
        print student['tests']

is equal to this piece of code

    for student in students:
        for item in student:
            print student[item]

<h4>The thing that take my 30 min to find and solve:</h4>

To find out how much the length of the list you need use 
  `len(listname)` command.
  
It will be repeat again but you will lose nothing to see it again. I am talking again about the taking the slice of strings and lists. The code is same for both of them; `"""nameofthestring[number:number] example==> letters[0:3]"""` 

the `del` command workss for deleting items from the dictionaries. Its is using like this `del dictionary_name[item_name]`

There will be some extra codes for deleting the item inside the list:
Removing elements from lists

This exercise will expand on ways to remove items from a list. You actually have a few options. For a list called<span class="Apple-converted-space"> </span>`n`:

1.  `n.pop(index)`<span class="Apple-converted-space"> </span>will remove the item at<span class="Apple-converted-space"> </span>`index`<span class="Apple-converted-space"> </span>from the list and return it to you:

```
n = [1, 3, 5]
n.pop(1)
# Returns 3 (the item at index 1)
print n
# prints [1, 5]
```

1.  `n.remove(item)`<span class="Apple-converted-space"> </span>will remove the actual<span class="Apple-converted-space"> </span>`item`<span class="Apple-converted-space"> </span>if it finds it:

```
n.remove(1)
# Removes 1 from the list,
# NOT the item at index 1
print n
# prints [3, 5]
```

1.  `del(n[1])`<span class="Apple-converted-space"> </span>is like<span class="Apple-converted-space"> </span>`.pop`<span class="Apple-converted-space"> </span>in that it will remove the item at the given index, but it won't return it:

```
del(n[1])
# Doesn't return anything
print n
# prints [1, 5]
```

---------------

<h2>Range Function</h2>

Passing a range into a function

Okay! Range time. The Python<span class="Apple-converted-space"> </span>`range()`function is just a shortcut for generating a list, so you can use ranges in all the same places you can use lists.

```
range(6) # => [0,1,2,3,4,5]
range(1,6) # => [1,2,3,4,5]
range(1,6,3) # => [1,4]
```

The<span class="Apple-converted-space"> </span>`range`<span class="Apple-converted-space"> </span>function has three different versions:

1.  **range**(*stop*)
2.  **range**(*start*,<span class="Apple-converted-space"> </span>*stop*)
3.  **range**(*start*,<span class="Apple-converted-space"> </span>*stop*,<span class="Apple-converted-space"> </span>*step*)

In all cases, the<span class="Apple-converted-space"> </span>`range()`<span class="Apple-converted-space"> </span>function returns a list of numbers from<span class="Apple-converted-space"> </span>*start*<span class="Apple-converted-space"> </span>up to (but not including)<span class="Apple-converted-space"> </span>*stop*. Each item increases by<span class="Apple-converted-space"> </span>*step*.

If omitted,<span class="Apple-converted-space"> </span>*start*<span class="Apple-converted-space"> </span>defaults to zero and<span class="Apple-converted-space"> </span>*step*<span class="Apple-converted-space"> </span>defaults to one.

<h2>Import Random Integer</h2>

```
from random import randint
coin = randint(0, 1)
dice = randint(1, 6)
```

1.  In the above example, we first import the<span class="Apple-converted-space"> </span>`randint(low, high)`function from the<span class="Apple-converted-space"> </span>`random`<span class="Apple-converted-space"> </span>module.
2.  Then, we generate either zero or one and store it in<span class="Apple-converted-space"> </span>`coin`.
3.  Finally, we generate a number from one to six inclusive.



<h2>Reminding One More time Taking an Input from the Client</h2>


```
number = raw_input("Enter a number: ")
if int(number) == 0:
    print "You entered 0"
```

`raw_input`<span class="Apple-converted-space"> </span>asks the user for input and returns it as a string. But we're going to want to use integers for our guesses! To do this, we'll wrap the<span class="Apple-converted-space"> </span>`raw_input`s with<span class="Apple-converted-space"> </span>`int()`<span class="Apple-converted-space"> </span>to convert the string to an integer.

<h1>Loops</h1> 

**While-Do**<br/>
```
loop_condition = True

while loop_condition:
    print "I am a loop"
    loop_condition = False
```
<note>**Breaking the Loop**</note>
```
while True:
    print count
    count += 1
    if count >= 10:
        break
```
<h2>Taking an Integer Input</h2>
`guess = int(raw_input("Your guess: "))`<br/>
Remember, raw_input turns user input into a string, so we use int() to make it a number again.
<h2>Enumerate Function</h2>
`enumerate`<span style="color: rgb(51, 51, 51); font-family: &quot;Open Sans&quot;, &quot;Hevetica Neue&quot;, Helvetica, sans-serif; font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); display: inline !important; float: none;"><span class="Apple-converted-space"> </span>works by supplying a corresponding index to each element in the list that you pass it. Each time you go through the loop,<span class="Apple-converted-space"> </span></span>`index`<span style="color: rgb(51, 51, 51); font-family: &quot;Open Sans&quot;, &quot;Hevetica Neue&quot;, Helvetica, sans-serif; font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); display: inline !important; float: none;"><span class="Apple-converted-space"> </span>will be one greater, and<span class="Apple-converted-space"> </span></span>`item`<span style="color: rgb(51, 51, 51); font-family: &quot;Open Sans&quot;, &quot;Hevetica Neue&quot;, Helvetica, sans-serif; font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); display: inline !important; float: none;"><span class="Apple-converted-space"> </span>will be the next item in the sequence. It's very similar to using a normal<span class="Apple-converted-space"> </span></span>`for`<span style="color: rgb(51, 51, 51); font-family: &quot;Open Sans&quot;, &quot;Hevetica Neue&quot;, Helvetica, sans-serif; font-size: 15px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); display: inline !important; float: none;"><span class="Apple-converted-space"> </span>loop with a list, except this gives us an easy way to count how many items we've seen so far.</span>







