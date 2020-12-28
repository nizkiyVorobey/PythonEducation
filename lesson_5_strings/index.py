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

# str = 'second item {unitList[1]}'.format(unitList=[1,2,3]) #second item 2

# print(str)

# num = "000000000000435"
# print(num.strip('0')) #435

# num = "1241410094"
# print(num.strip('1299')) #41410094


# Сырые строки
# Написав вначале строки символ r мы можем не экранировать спец. символы
# str = "File on didsk C:\\\\"
# print(str) #File on didsk C:\\

# str = r"File on didsk C:\\"
# print(str) #File on didsk C:\\

# str = "Hello world" * 3
# print(str) #Hello worldHello worldHello world


# # Строки неизменяемы
# #Адрес памяти мы можем запросить с помощю фкнции id
# str1 = "Hello"
# print(id(str1)) # 4355269136
# str1 += ", world" #4355269184
# print(id(str1))
# # Как видим это разные


# # Срезы строк
# str = "Course about Python on Coursera"
# print(str[7:]) # about Python on Coursera
# print(str[7:13]) # about
# print(str[-8:]) # Coursera

# str = '0123456789'
# print(str[::2]) # 02468. Step is 2

# str = 'Hello world'
# print(str[::-1]) # dlrow olleH. Таким смопобом можно разернкть строку


# # Methods
# str = """
# Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
# Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
# Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
# Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
# """
# print(str.count('o')) # 29. Сколько раз в строке встертилась буква o

# print('senya'.capitalize()) #Senya
# print('2017'.isdigit()) # True
# print('0'.isdigit()) # True
# print('-1'.isdigit()) # False
# print('1i'.isdigit()) # False
# print('1 * 2'.isdigit()) # False


# # Опертор in позволяет узнать содердится ли стока в подстроке
# result = '3.14' in 'Число ПИ = 3.144415152'
# print(result) # True

# # Оператор for..in позволяет итерироватьсЯ по строке
# str = 'Hello'
# for letter in str:
#     print("Letter mow is: ", letter)
# # ('Letter mow is: ', 'H')
# # ('Letter mow is: ', 'e')
# # ('Letter mow is: ', 'l')
# # ('Letter mow is: ', 'l')
# # ('Letter mow is: ', 'o')


# # конверация типов
# myStr = str(12.0)
# print(type(myStr)) # <type 'str'>
# print(bool('not wmpty string')) # True
# print(bool("")) # False


# # ФОрматирование строк
# myStr = "{}, это было {}. ({})".format(
#     "Саня", "чудесно", "Rober Wright"
# )
# print(myStr) # Саня, это было чудесно. (Rober Wright)

# myStr = "{num}kB it is enought for this {name}".format(
#     num=640, name="file"
# ) 
# print(myStr) # 640kB it is enought for this file

# subject = 'math'
# author = 'Senya'
# myStr = f"{author} learnd {subject} in school"
# print(myStr) # Senya learnd math in school


# # Модификаторы
# num = 8
# myStr = f"Binary: {num:#b}" #Binary: 0b1000
# print(myStr)

# num = 2 / 3
# print(num) # 0.6666666666666666
# print(f'{num:.3f}') # 0.667


# name = input('input yout name: ')
# print(f"Your name is {name}")
# # input yout name: Senya
# # Your name is Senya



# # Байтовые строки.
# # Что бы обявить байтовую строку используется литера b
# # Байтровая трока єто послдеовательность чисел от 0 до 255
# myStr = b"Hello"
# print(myStr) # b'Hello'
# print(type(myStr)) # <class 'bytes'>

# for byte in myStr:
#     print(byte)
# # 72
# # 101
# # 108
# # 108
# # 111

# myStr = b"привет" # error. Нужно использовать кодировку

# myStr = "привет"
# myStr = myStr.encode(encoding='utf-8')
# print(type(myStr)) # <class 'bytes'>
# print(myStr) # b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
# # но utf-8 идет по дкфолту так что можно просто так
# myStr = myStr.encode()
# print(myStr) # b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'

# #Что бы разкодировать строку испльзуем метод decode
# decodeStr = myStr.decode()
# # или можно наявно указать какая кодировка
# # decodeStr = myStr.decode(encoding='utf-8')
# print(decodeStr) # привет