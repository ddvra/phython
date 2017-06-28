Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=["one","two"]
>>> a
['one', 'two']
>>> a1
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a1
NameError: name 'a1' is not defined
>>> a 1
SyntaxError: invalid syntax
>>> a"1"
SyntaxError: invalid syntax
>>> a[1]
'two'
>>> mystock = []
>>> my
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    my
NameError: name 'my' is not defined
>>> mystock
[]
>>> jangdeok=[]
>>> jangdeok
[]
>>> jangdeok.append('홍은철')
>>> ㅓ뭏ㅇ대ㅏ
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    ㅓ뭏ㅇ대ㅏ
NameError: name 'ᅥ뭏ᄋ대ᅡ' is not defined
>>> jangdeok
['홍은철']
>>> jankdeok.append('이서준')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    jankdeok.append('이서준')
NameError: name 'jankdeok' is not defined
>>> jangdeok.append('이서준')
>>> jangdeok
['홍은철', '이서준']
>>> jangdeok.append('최태현')
>>> j
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    j
NameError: name 'j' is not defined
>>> jangdeok
['홍은철', '이서준', '최태현']
>>> jangdeok.pop()
'최태현'
>>> del jangdeok[1]
>>> jangdeok
['홍은철']
>>> jangdeok.delete(2)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    jangdeok.delete(2)
AttributeError: 'list' object has no attribute 'delete'
>>> jangdeok.del(0)
SyntaxError: invalid syntax
>>> del
SyntaxError: invalid syntax
>>> del
SyntaxError: invalid syntax
>>> jangdeok.delete(0)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    jangdeok.delete(0)
AttributeError: 'list' object has no attribute 'delete'
>>> jangdeok.remove(2)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    jangdeok.remove(2)
ValueError: list.remove(x): x not in list
>>> jangdeok.remove('홍은철
		
SyntaxError: EOL while scanning string literal
>>> jangdeok.remove('홍은철')
>>> jangdeok
[]
>>> jangdeok.insert(1,'박판성')
>>> jangdeok
['박판성']
>>> jangdeok.insert(0,'홍은철')
>>> jangdeok
['홍은철', '박판성']
>>> jangdeok.sort()
>>> jangdeok
['박판성', '홍은철']
>>> jangdeok.reverse()
>>> jangdeok
['홍은철', '박판성']
>>> 
