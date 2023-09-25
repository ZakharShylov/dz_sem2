#Task 22
# n=(int(input("Введите число N элементов: ")))
# num_list_1=[]
# for i in range(n):
#     num = int(input("Введите num "))
#     num_list_1.append(num)
# print(num_list_1)


# m=(int(input("Введите число M элементов: ")))
# num_list_2 = []
# for i in range(m):
#     num = int(input("Введите num "))
#     num_list_2.append(num)
# print(num_list_2)


# num_list3 = num_list_1+num_list_2

# print(num_list3)
# checked_nums_list = []
# for i in num_list3:
#     if num_list3.count(i) > 1 and i not in checked_nums_list:
#         checked_nums_list.append(i)
#         print(i)

# Task 24

# n_bushes = int(input('Введите количество кустов черники: '))
# arr = list()
# for i in range(n_bushes):
#     a =int(input('Введите количество ягод на кусте: '))
#     arr.append(a)

# arr_count = list()
# for i in range(len(arr)):
#        arr_count.append(arr[i-2] + arr[i-1] + arr[i])
# print(max(arr_count))