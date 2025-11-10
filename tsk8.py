def sort_string(s):
    char_list = list(s)
    char_list.sort()
    sorted_string = ''.join(char_list)
    return sorted_string

input_string = input("Введите строку: ")
result = sort_string(input_string)
print("Отсортированная строка:", result)
