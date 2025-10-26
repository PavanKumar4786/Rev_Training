Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> not 0
True
>>> not -2
False
>>> 7&9
1
>>> 7|9
15
>>> 7^9
14
>>> 5<<3
40
>>> 5<<4
80
>>> 5>>2
1
>>> 5>>3
0
>>> 5>>>3
SyntaxError: invalid syntax
>>> 5
5
>>> 



>>> 

>>> 


>>> 

>>> 


>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 5>>>>4
SyntaxError: invalid syntax
>>> num1 is int
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    num1 is int
NameError: name 'num1' is not defined
>>> num1 = 2
>>> num1 is int
False
>>> type(num1) is int
True
>>> type(num1) is  not str
True
>>> print(num1)
2
>>> print('hi')
hi
>>> 'hi'
'hi'
>>> print("hi")
hi
>>> "hi"
'hi'
>>> print('hi' + 'hello')
hihello
>>> print(num1+10)
12
>>> print(num+'num')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print(num+'num')
NameError: name 'num' is not defined
>>> print(num1+'num')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print(num1+'num')
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
>>> print(num1+10)
12
>>> print(num1+'10')
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print(num1+'10')
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print('hi'+10)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    print('hi'+10)
TypeError: can only concatenate str (not "int") to str
>>> print('sum : ' + 10)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print('sum : ' + 10)
TypeError: can only concatenate str (not "int") to str
>>> print('sum : ' + num1+ 10)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print('sum : ' + num1+ 10)
TypeError: can only concatenate str (not "int") to str
>>> print('sum : ', num1+ 10)
sum :  12
>>> print('sum : '+ '/n', num1+ 10)
sum : /n 12
>>> print('sum : '+ '\n', num1+ 10)
sum : 
 12
>>> print('name :' + pavaan)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    print('name :' + pavaan)
NameError: name 'pavaan' is not defined
>>> print('name :' , pavaan)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    print('name :' , pavaan)
NameError: name 'pavaan' is not defined
>>> print('name :' ,= pavan)
SyntaxError: invalid syntax
>>> print('name :' ,+ pavan)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    print('name :' ,+ pavan)
NameError: name 'pavan' is not defined
>>> print('name :' ,+ num1)
name : 2
>>> print('name :' ,+ 4)
name : 4
>>> input()
3
'3'
>>> input()
pavan
'pavan'
>>> input()
true
'true'
>>> input('enter a num')
enter a num 6
' 6'
>>> input('enter a num:')
enter a num: 3
' 3'
>>> input('enter a num:')
enter a num:9
'9'
>>> int(input('enetr a num:))
	  
SyntaxError: EOL while scanning string literal
>>> int(input('enter a num:))
	  
SyntaxError: EOL while scanning string literal
>>> int(input('enter a num:'))
enter a num:5
5
>>> float(iinput('enetr a num:'))
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    float(iinput('enetr a num:'))
NameError: name 'iinput' is not defined
>>> float(iinput('enter a num:'))
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    float(iinput('enter a num:'))
NameError: name 'iinput' is not defined
>>> float(input('enter a num:'))
enter a num:3
3.0
>>> bool(input('enter a num:'))
enter a num:3
True
>>> bool(input('enter a num:'))
enter a num:0
True
>>> bool(input('enter a num:'))
enter a num:1
True
>>> bool(input('enter a num:'))
enter a num:-1
True
>>> bool(true)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    bool(true)
NameError: name 'true' is not defined
>>> bool('true')
True
>>> bool()
False
>>> bool(0)
False
>>> 'hi'
'hi'
>>> 
>>> 
>>> "hi"
'hi'
>>> "ram's home"
"ram's home"
>>> 'ram's house'
SyntaxError: invalid syntax
>>> 'ram"s home'
'ram"s home'
>>> str1="hello hi !"
>>> len(str1)
10
>>> str[0]
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    str[0]
TypeError: 'type' object is not subscriptable
>>> str1[0]
'h'
>>> str1[11]
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    str1[11]
IndexError: string index out of range
>>> str1[5]
' '
>>> str[-1]
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    str[-1]
TypeError: 'type' object is not subscriptable
>>> str1[-1]
'!'
>>> str1=str
>>> str[0:3]
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    str[0:3]
TypeError: 'type' object is not subscriptable
>>> str1[0:3]
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    str1[0:3]
TypeError: 'type' object is not subscriptable
>>> str="hello hi !"
>>> str[0:3]
'hel'
>>> str[o:]
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    str[o:]
NameError: name 'o' is not defined
>>> str[0:]
'hello hi !'
>>> str[:-1]
'hello hi '
>>> str[0:8:2]
'hloh'
>>> str[::4]
'ho '
>>> str[::2]
'hloh '
>>> str[-2:-6]
''
>>> str[-6:-2]
'o hi'
>>> str[-8:-1:2]
'loh '
>>> str
'hello hi !'
>>> str.capitalize()
'Hello hi !'
>>> str.rstrip()
'hello hi !'
>>> str.casefold()
'hello hi !'
>>> str.count()
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    str.count()
TypeError: count() takes at least 1 argument (0 given)
>>> 
>>> str.count('h')
2
>>> str.count('1')
0
>>> str.count(0)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    str.count(0)
TypeError: must be str, not int
>>> str.endswith('!')
True
>>> str.endswith('h')
False
>>> str.startswith('h')
True
>>> str.startswith('-1')
False
>>> str.find('-1)
	 
SyntaxError: EOL while scanning string literal
>>> str.find('-1')
-1
>>> str.find('')
0
1
>>> str.find('-1')
-1
>>> str.find('!')
9
>>> str.find('2')
-1
>>> str.title()
'Hello Hi !'
>>> str.translate('H')
'hello hi !'
>>> str.translate('e')
'hello hi !'
>>> str.swapcase()
'HELLO HI !'
>>> str.encode('utf-16')
b'\xff\xfeh\x00e\x00l\x00l\x00o\x00 \x00h\x00i\x00 \x00!\x00'
>>> str.encode('utf-32')
b'\xff\xfe\x00\x00h\x00\x00\x00e\x00\x00\x00l\x00\x00\x00l\x00\x00\x00o\x00\x00\x00 \x00\x00\x00h\x00\x00\x00i\x00\x00\x00 \x00\x00\x00!\x00\x00\x00'
>>> str.encode('utf-128')
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    str.encode('utf-128')
LookupError: unknown encoding: utf-128

>>> str.encode('utf-64')
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    str.encode('utf-64')
LookupError: unknown encoding: utf-64
>>> str.encode('utf-0')
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    str.encode('utf-0')
LookupError: unknown encoding: utf-0
>>> print(ord('Hello')
      h
      
SyntaxError: invalid syntax
>>> print(ord("hello")
      hello
      
SyntaxError: invalid syntax
>>> print(ord("hello"))
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    print(ord("hello"))
TypeError: ord() expected a character, but string of length 5 found
>>> print(ord("k"))
107
>>> str.replace('o', '0')
'hell0 hi !'

>>> str.split('-')
['hello hi !']
>>> str1=10-2-2025
>>> str1.split()
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    str1.split()
AttributeError: 'int' object has no attribute 'split'
>>> str1.split('-')
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    str1.split('-')
AttributeError: 'int' object has no attribute 'split'
>>> str1='10-2-2025'
>>> str1.split('-')
['10', '2', '2025']
>>> str.join(str1)
'1hello hi !0hello hi !-hello hi !2hello hi !-hello hi !2hello hi !0hello hi !2hello hi !5'
>>> str.join(str1)
'1hello hi !0hello hi !-hello hi !2hello hi !-hello hi !2hello hi !0hello hi !2hello hi !5'
>>> str1=hello
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    str1=hello
NameError: name 'hello' is not defined
>>> str1='hello'
>>> id(str)
1919518028080
>>> str1='india'
>>> id(str1)
1919518014464
>>> numberds=[10, 20, 30]
>>> numbers=[10, 20, 30]
>>> id(numbers)
1919517808520
>>> numbers.append(40)
>>> numbers
[10, 20, 30, 40]
>>> id(numbers)
1919517808520
>>> numbers.append(40)
>>> numberd
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    numberd
NameError: name 'numberd' is not defined
>>> numbers
[10, 20, 30, 40, 40]
>>> numbers[2]
30
>>> numbers[3]=100
>>> numbers
[10, 20, 30, 100, 40]
>>> numbers.append(40)
>>> numbers.count(40)
2
>>> numbers.index(20)
1
>>> numbers.index(40)
4
>>> numbers.insert(4, 500)
>>> numbers
[10, 20, 30, 100, 500, 40, 40]
>>> numbers.remove(40)
>>> numbers
[10, 20, 30, 100, 500, 40]
>>> numbers.remove(500,40)
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    numbers.remove(500,40)
TypeError: remove() takes exactly one argument (2 given)
>>> numbers.remove(500)
>>> numbers
[10, 20, 30, 100, 40]
>>> numbers.remove(100)
>>> numbers
[10, 20, 30, 40]
>>> numbers.pop()
40
>>> numbers
[10, 20, 30]
>>> numbers.pop(-2)
20
>>> numbers
[10, 30]
>>> numbers.insert(20, 2)
>>> numbers
[10, 30, 2]
>>> numbers.insert(2, 20)
>>> numbers
[10, 30, 20, 2]
>>> numbers.reverse()
>>> numbers
[2, 20, 30, 10]
>>> numbers.sort()
>>> numbers
[2, 10, 20, 30]
>>> numbers.sort(-1)
Traceback (most recent call last):
  File "<pyshell#189>", line 1, in <module>
    numbers.sort(-1)
TypeError: sort() takes no positional arguments
>>> numbers.sort(reverse=True)
>>> numbers
[30, 20, 10, 2]
>>> numbers.copy()
[30, 20, 10, 2]
>>> nums=numbers.copy()
>>> nums
[30, 20, 10, 2]
>>> id(nums)
1919518029128
>>> id(numbers)
1919517808520
>>> nums1=numbers
>>> id(nums1)
1919517808520
>>> numbers.extend(nums)
>>> numbes
Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    numbes
NameError: name 'numbes' is not defined
>>> numbers
[30, 20, 10, 2, 30, 20, 10, 2]
>>> numbers.clear()
>>> numbers
[]
>>> del()
>>> tup1=(10, 20, 30)
>>> tup[2]
Traceback (most recent call last):
  File "<pyshell#206>", line 1, in <module>
    tup[2]
NameError: name 'tup' is not defined
>>> tup1[2]
30
>>> tuple.clear()
Traceback (most recent call last):
  File "<pyshell#208>", line 1, in <module>
    tuple.clear()
AttributeError: type object 'tuple' has no attribute 'clear'
>>> tupl.clear()
Traceback (most recent call last):
  File "<pyshell#209>", line 1, in <module>
    tupl.clear()
NameError: name 'tupl' is not defined
>>> tupl1.clear()
Traceback (most recent call last):
  File "<pyshell#210>", line 1, in <module>
    tupl1.clear()
NameError: name 'tupl1' is not defined
>>> set1={22, 11, 33, 55, 9, 7}
>>> set1
{33, 7, 9, 11, 22, 55}
>>> set1.add(43)
>>> set1
{33, 7, 9, 11, 43, 22, 55}
>>> set2={10,20,30,40}
>>> set1.union(set2)
{33, 7, 40, 9, 10, 11, 43, 20, 22, 55, 30}
>>> set1.difference(set2)
{33, 7, 9, 11, 43, 22, 55}
>>> set2.difference(set1)
{40, 10, 20, 30}
>>> set1
{33, 7, 9, 11, 43, 22, 55}
>>> set2
{40, 10, 20, 30}
>>> set3=set1.union(set2)
>>> set3
{33, 7, 40, 9, 10, 11, 43, 20, 22, 55, 30}
>>> set3.intersection()
{33, 7, 40, 9, 10, 11, 43, 20, 22, 55, 30}
>>> set4=set3.intersection(set2)
>>> set4
{40, 10, 20, 30}
>>> set5=det1.difference(set4)
Traceback (most recent call last):
  File "<pyshell#227>", line 1, in <module>
    set5=det1.difference(set4)
NameError: name 'det1' is not defined
>>> set5=set1.difference(set4)
>>> set4
{40, 10, 20, 30}
>>> set5
{33, 7, 9, 11, 43, 22, 55}
>>> set1.discard(33)
>>> set1
{7, 9, 11, 43, 22, 55}
>>> dict={1:10,2:20}
>>> dict
{1: 10, 2: 20}
>>> dict[2]
20
>>> dict[3]
Traceback (most recent call last):
  File "<pyshell#236>", line 1, in <module>
    dict[3]
KeyError: 3
>>> dict1[2] = 200
Traceback (most recent call last):
  File "<pyshell#237>", line 1, in <module>
    dict1[2] = 200
NameError: name 'dict1' is not defined
>>> dict1 [2] = 200
Traceback (most recent call last):
  File "<pyshell#238>", line 1, in <module>
    dict1 [2] = 200
NameError: name 'dict1' is not defined
>>> dict[2] = 200
>>> dict
{1: 10, 2: 200}
>>> dict2={'rno':'123','name':'AAA'}
>>> dict2[2]
Traceback (most recent call last):
  File "<pyshell#243>", line 1, in <module>
    dict2[2]
KeyError: 2
>>> dict[rno]
Traceback (most recent call last):
  File "<pyshell#244>", line 1, in <module>
    dict[rno]
NameError: name 'rno' is not defined
>>> dict['rno']
Traceback (most recent call last):
  File "<pyshell#245>", line 1, in <module>
    dict['rno']
KeyError: 'rno'
>>> dict2['rno']
'123'
>>> dict2['ph']=9346671608
>>> dict2
{'rno': '123', 'name': 'AAA', 'ph': 9346671608}
>>> dict1.get('ph')
Traceback (most recent call last):
  File "<pyshell#249>", line 1, in <module>
    dict1.get('ph')
NameError: name 'dict1' is not defined
>>> dict1.get('ph')
Traceback (most recent call last):
  File "<pyshell#250>", line 1, in <module>
    dict1.get('ph')
NameError: name 'dict1' is not defined
>>> dict2.get('ph')
9346671608
>>> dict2.keys()
dict_keys(['rno', 'name', 'ph'])
>>> dict2.values()
dict_values(['123', 'AAA', 9346671608])
>>> dict2.pop(123)
Traceback (most recent call last):
  File "<pyshell#254>", line 1, in <module>
    dict2.pop(123)
KeyError: 123
>>> dict2.pop(rno)
Traceback (most recent call last):
  File "<pyshell#255>", line 1, in <module>
    dict2.pop(rno)
NameError: name 'rno' is not defined
>>> dict2.pop('rno')
'123'
>>> dict2
{'name': 'AAA', 'ph': 9346671608}
>>> 
