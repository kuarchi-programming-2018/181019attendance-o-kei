# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""
def fib(n):
#フィボナッチ数列を定義する。
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a + b
    return b


print([fib(i) for i in range(10)]) 
L = []
for i in range(10):
    L.append(fib(i))
print(L)
#n=1,2,3...,10の時のフィボナッチ数列
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print(fib(2)) 