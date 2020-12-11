#! /usr/bin/env python
# -*- coding: utf-8 -*-

# s = 'smam"s'
# print(s) # sam"s

# str = "Incididunt velit incididunt \nconsectetur Lorem deserunt quis magna exercitation veniam voluptate enim veniam ad. \fMollit minim ea labore nisi dolore qui. Pariatur veniam id nostrud et elit commodo commodo Lorem ipsum dolore sint nulla eu qui. Nostrud ea ad consequat reprehenderit voluptate eiusmod laborum magna enim veniam."
# print(str)

# str = '''
# Hello
#     I'am multi
#     row text
# '''
# print(str) # сохраняет табуляциию и переносы строк
# print(len(str)) # 35

# # str = 'Hello'
# print(len(str)) #5


# str = 'messages'
# print(str[1]) # e
# print(str[2:5]) # ssa
# print(str[1:]) # essages


# str = 'test'
# str.replace('e', 'X')
# print(str) # test

# print(str.replace('e', 'X')) #tXst

# str = 'Hello'
# sp = str.split('') # error
# sp = str.split('e') # ['H', 'llo']
# sp = str.split(' ') # ['Hello']
# print(sp)

# # Форматирование строк с помощью метода format
# str = 'Hello {}'.format('Senya')
# print(str) # Hello Senya

# str = "number row contaion of {}, {}, {}".format(1,2,3) # number row contaion of 1, 2, 3
# str = "number row contaion of {0}, {1}, {2}".format(1,2,3) # number row contaion of 1, 2, 3
# str = "number row contaion of {2}, {1}, {0}".format(1,2,3) # number row contaion of 3, 2, 1
# str = "number row contaion of {5}, {1}, {2}".format(1,2,3) # error

# str = "number row contaion of {0}, {1}, {0}".format('one', 'two') # number row contaion of one, two, one
# str = "number row contaion of {2}, {1}, {0}".format(*'abc') # number row contaion of c, b, a

# str = 'coordinates id {latitude}, {longitude}'.format(longitude="123N", latitude=122) # coordinates id 122, 123N

str = 'second item {unitList[1]}'.format(unitList=[1,2,3]) #second item 2

print(str)

# num = "000000000000435"
# print(num.strip('0')) #435

# num = "1241410094"
# print(num.strip('1299')) #41410094