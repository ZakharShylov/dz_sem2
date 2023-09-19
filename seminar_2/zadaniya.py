# #Task9
# n = int(input('Введите целое число '))
# k = 1
# while n > 0:
#     k *= n # result = result * n 
#     n = n - 1
#     print(k)

#Task11

# n = int(input('Введите число '))

# fib1 = 0
# fib2 = 1

# i = 2
# while fib2 < n:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i = i + 1
#     if fib2 > n:
#         i =-1

 
# print(i)

# Task 15
# n = int(input("Введите кол-во арбузов: "))
# x = int(input("Введите массу арбуза: "))
# max_massa = min_massa = x
# for i in range(n - 1): 
#     x = int(input("Введите массу арбуза: "))
#     if max_massa < x:
#         max_massa = x
#     elif min_massa > x: 
#         min_massa = x
# print(min_massa, max_massa)


# Task 13
# n = int(input("Введите кол-во дней: "))
# count = 0
# max_count = 0
# for i in range(n):
#     temp = int(input("Введите температуру: "))
#     if temp > 0:
#         count += 1
#         if max_count < count:
#             max_count = count
#     else:
#         count = 0
# print(max_count)
