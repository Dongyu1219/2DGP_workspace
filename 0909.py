Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
title = 'Python'
title[0]
'P'
title[-1]
'n'
title[2:4]
'th'
title[:]
'Python'
title[-2]
'o'
title[-2:]
'on'


twice = [ 'momo', 'sana' , 'zwi']
#리스트 초기화

type(twice)
<class 'list'>
len(twice)
3
#3명

twice.append('jihyo')
twice
['momo', 'sana', 'zwi', 'jihyo']
len(twice)
4
twice,sort()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    twice,sort()
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
twice.sort()
twice
['jihyo', 'momo', 'sana', 'zwi']
twice[0]
'jihyo'
twice[3]
'zwi'
twice[2]
'sana'
twice[-1]
'zwi'
black_pink = ['jisu', 'jeni', 'rose']
len(black_pink)
3

unite = twice + black_pink
len(unite)
7
type(unite)
<class 'list'>
#리스트와 리스트는 더할 수 있다

unite.sort()
unite[0]
'jeni'
unite[:3]
['jeni', 'jihyo', 'jisu']

best3=unite[:3]
best3
['jeni', 'jihyo', 'jisu']
low3
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    low3
NameError: name 'low3' is not defined
low3 = unite[-3:]
low3
['rose', 'sana', 'zwi']
unite.remove('momo')
unite.insert(0, 'daehyun')
unite
['daehyun', 'jeni', 'jihyo', 'jisu', 'rose', 'sana', 'zwi']
del.unite[-1]
SyntaxError: invalid syntax
del unite[-1]
unite
['daehyun', 'jeni', 'jihyo', 'jisu', 'rose', 'sana']
#파이썬은 리스트 자료구조가 내장되어있다
['daehyun', 'jeni', 'jihyo', 'jisu', 'rose', 'sana']
['daehyun', 'jeni', 'jihyo', 'jisu', 'rose', 'sana']




score = {'momo':80 , , 'ziwi': 85  , 'sana':98   }
SyntaxError: invalid syntax

score = {'momo':80, 'ziwi': 85  , 'sana':98   }
type(score)
<class 'dict'>
score['momo'}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
score['momo']
80
score[momo]
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    score[momo]
NameError: name 'momo' is not defined
score['ziwi']
85
score['jeni']=100
>>> score['jeni']
100
>>> score.sort()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    score.sort()
AttributeError: 'dict' object has no attribute 'sort'
>>> #dictionary sort 불가
>>> AttributeError: 'dict' object has no attribute 'sort'#dictionary sort 불가
SyntaxError: invalid syntax
>>> 
>>> len(socre)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    len(socre)
NameError: name 'socre' is not defined. Did you mean: 'score'?
>>> len(score)
4
>>> score.values()
dict_values([80, 85, 98, 100])
>>> sum([1,2,3,4,5,6,7,8,9,10])
55
>>> #sum은 리스트 안에 있은 값을 모두 더하는 함수
>>> total = sum(score.values())
>>> total
363
>>> avg = total / len(score)
>>> avg
90.75
>>> 363/4
90.75
>>> 
>>> #tuple : 상수( 값을 바꿀 수 없음)
>>> #시험에 나옴
>>> 
>>> #set: 집합
>>> #중복허용, 순서가 없음
>>> #시험
>>>
#파이썬에서는 4개의 자료구조가 내장되어있기 때문에 따로 만들어 쓰지 않아도 된다.

