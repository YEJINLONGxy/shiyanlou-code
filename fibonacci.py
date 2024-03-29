#!/usr/bin/env python3

#试试打印斐波那契数列。这个数列前两项为 1，之后的每一个项都是前两项之和。
#所以这个数列看起来就像这样：1,1,2,3,5,8,13 ......

a, b = 0, 1
while b < 100:
	print(b, end=" ")
	a, b = b, a + b
print()

#第一行代码中我们初始化 a 和 b。当 b 的值小于 100 的时候，
#循环执行代码。循环里我们首先打印 b 的值，然后在下一行将 a + b 的值赋值给 b，b 的值赋值给 a

#学习其他语言的同学在这里可能有些困惑，你可以这样理解，
#Python 中赋值语句执行时会先对赋值运算符右边的表达式求值，然后将这个值赋值给左边的变量。	

#默认情况下，print() 除了打印你提供的字符串之外，
#还会打印一个换行符，所以每调用一次 print() 就会换一次行，如同上面一样。
#你可以通过 print() 的另一个参数 end 来替换这个换行符
