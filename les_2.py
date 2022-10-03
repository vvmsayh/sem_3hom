# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
def mult_lst(myu_list):
    l = len(my_list)//2 + 1 if len(my_list) % 2 != 0 else len(my_list)//2
    new_lst = [my_list[i]*my_list[len(my_list)-i-1] for i in range(l)]
    print(new_lst)
my_list = [2, 3, 4, 5, 6]
mult_lst(my_list)
my_list = list(map(int, input("Введите числа через пробел:\n").split())) #для своего массива
mult_lst(my_list)
