sentence = input("Введите предложение: ")
words = sentence.split()
clean_words = []
signs = ".,!?;:()\"'"

for word in words:
    clean_word = word.strip(signs)  
    if clean_word:
        clean_words.append(clean_word)

print("Список слов без знаков препинания:", clean_words)
