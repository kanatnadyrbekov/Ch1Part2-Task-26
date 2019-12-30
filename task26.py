# Напишите функцию которая подсчитает количество счетных и несчетных чисел в списке
# чисел.

num = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
# num = int(input('---'))

a = [x for x in num if x % 2 == 0]
print(a)
c = len(a)
print("Len of the even ", c)
b = [x for x in num if x % 2 != 0]
print(b)
d = len(b)
print("Len of the odd ", d)