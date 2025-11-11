# Задание 10
list1_input = input("Введите элементы первого списка: ")
list2_input = input("Введите элементы второго списка: ")
start_idx = int(input("Введите начальный индекс диапазона: "))
end_idx = int(input("Введите конечный индекс диапазона: "))

lst1 = list(map(int, list1_input.split()))
lst2 = list(map(int, list2_input.split()))

elements_to_move = lst1[start_idx:end_idx+1]
lst2.extend(elements_to_move[::-1])
new_lst1 = lst1[:start_idx] + lst1[end_idx+1:]

print("Первый список после преобразований:", new_lst1)
print("Второй список после преобразований:", lst2)
