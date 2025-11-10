input_numbers = input("Введите целые числа через пробел: ")
numbers = input_numbers.split()

numbers_list = []
for n in numbers:
    numbers_list.append(int(n))

print("Список чисел:", numbers_list)

total = 0
for num in numbers_list:
    total += num
    
average = total / len(numbers_list)
print("Среднее значение:", average)
