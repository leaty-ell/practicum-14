input_string = input()

string_list = input_string.split()  
numbers_list = []
for s in string_list:
    numbers_list.append(int(s)) 
    
new_list = []
for num in numbers_list:
    if num != 3:
        new_list.append(num)

print("Исходный список:", numbers_list)
print("Список без троек:", new_list)
