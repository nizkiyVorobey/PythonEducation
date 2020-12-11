#! /usr/bin/env python
# -*- coding: utf-8 -*-

# def first(x):
#     print(x)

# first(22) # 22

# def test(x):
#     def test2(y):
#         return x + y
#     return test2

# res = test(2)(3)
# print(res) # 5

# ############################################################
# def test(a,b,c):
#     return [a,b,c]

# res = test(3,6,1)
# print(res) # [3, 6, 1]

# res = test(b=3, c=6,a=1)
# print(res) # [1, 3, 6]

# ############################################################
# def test (*args):
#     return args

# res = test(3,1,5)
# print(res) # (3, 1, 5)

# res = test(a=3,c=1,b=5)
# print(res) # error


# def test (**args): # can take named args
#     return args

# res = test(a=3,c=1,b=5)
# print(res) # {'a': 3, 'c': 1, 'b': 5}


# Анонимные функции, инструкция lambda
# func = lambda x,y: x + y
# print(func(3,4)) #7

# print(
#     (lambda x, y: x + y)(2, 1)
# )  # 3




# func = lambda *args: args
# print(
#     func(1,2,3,4,5)
# ) #(1, 2, 3, 4, 5)


# print(
#     sum([1,4,5],0)
# ) # 10

# print(
#     sum([1,4,5],5)
# ) # 15