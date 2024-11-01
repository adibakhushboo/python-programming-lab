Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

========== RESTART: C:/Users/Student/lists 58.py ==========
l
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

========== RESTART: C:/Users/Student/lists 58.py ==========
type(l)
<class 'list'>
l[0]
'a'
l[2:5]
['c', 'd', 'e']
len(l)
8
l.insert(3,'k')
l
['a', 'b', 'c', 'k', 'd', 'e', 'f', 'g', 'h']
l.append('M')
l
['a', 'b', 'c', 'k', 'd', 'e', 'f', 'g', 'h', 'M']
l.append('M')
l
['a', 'b', 'c', 'k', 'd', 'e', 'f', 'g', 'h', 'M', 'M']
l.count('M')
2
l.count('a')
1
l.remove('M')
l
['a', 'b', 'c', 'k', 'd', 'e', 'f', 'g', 'h', 'M']
l.insert(2,'l')
l
['a', 'b', 'l', 'c', 'k', 'd', 'e', 'f', 'g', 'h', 'M']
del l
l
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    l
NameError: name 'l' is not defined
l=['a','b','c','d','e']
l.reverse()
l
['e', 'd', 'c', 'b', 'a']
l.sort()
l
['a', 'b', 'c', 'd', 'e']
b=[1,5,9,8,0]
b.sort()
b
[0, 1, 5, 8, 9]
[0, 1, 5, 8, 9]
[0, 1, 5, 8, 9]
s="hello"
print(s[::-1])
olleh
print(s[1:3])
el
print(s[2:5])
llo
import random
nums=[1,2,3,4,5]
random.shuffle(nums)
print(nums)
[2, 1, 3, 5, 4]
print(nums)
[2, 1, 3, 5, 4]
random.shuffle
<bound method Random.shuffle of <random.Random object at 0x000001CA2BDA7020>>
random.shuffle(nums)
nums
[1, 3, 5, 4, 2]
l1=['a','b','c','d']
>>> l2=[1,2,'c','d']
>>> l1+l2
['a', 'b', 'c', 'd', 1, 2, 'c', 'd']
>>> l1[:3]
['a', 'b', 'c']
>>> l2[:]
[1, 2, 'c', 'd']
>>> l2[::-1]
['d', 'c', 2, 1]
>>> l2[::1]
[1, 2, 'c', 'd']
>>> l1[::2]
['a', 'c']
>>> l2[::2]
[1, 'c']
>>> l1[::4]
['a']
