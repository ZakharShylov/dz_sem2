# name = "Ivan"
# # 0123
# print(name[0])

for elemnt in "Hello" , 123, 32.125, True, 'a':
    print(elemnt)
# 0: elemt = "Hello"
# 1: ekemnt = 123
# ...
# range и for между собой НИКАК НЕ СВЯЗАНЫ!!
# range(begin=необязательний(0), end=обязательный, step=необязательный(+1))
print(*range(5))
# 0 1 2 3 4
print(*range(5, 0, -1))
print(*range(5,13,2))
print(*range(2, 10))
print(*range(0, 8, 2))

# for i in range(5):
#     print(i, end=' ')

print(1, end=', ')
print(2, end='. ')
print(3, end='!\n')
#print()
print("Hello")

print("Ivan")

