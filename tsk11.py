numbers_input = input("Введите элементы списка: ")
command = input("Введите команду: ")

numbers = list(map(int, numbers_input.split()))

direction = command[0]
positions = int(command[1:])

if direction == 'R':
    shift = positions % len(numbers)
    result = numbers[-shift:] + numbers[:-shift]
elif direction == 'L':
    shift = positions % len(numbers)
    result = numbers[shift:] + numbers[:shift]
else:
    result = numbers

print("Результат:", result)
