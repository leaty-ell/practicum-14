def sort_string(s):
    """Sort characters in a string in alphabetical order.
    Args:
        s (str): The input string to be sorted.
    Returns:
        str: The sorted string with characters in alphabetical order.
    """
    char_list = list(s)
    char_list.sort()
    sorted_string = ''.join(char_list)
    return sorted_string


def main():
    """
    Main program function.
    """
    input_string = input("Введите строку: ")
    result = sort_string(input_string)
    print("Отсортированная строка:", result)


if __name__ == "__main__":
    main()
