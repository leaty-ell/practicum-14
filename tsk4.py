sentence = input("Введите предложение: ")
words = sentence.split()
unique_words = []
signs = ".,!?;:()\"'"

for word in words:
    clean_word = word.strip(signs).lower()
    
    if clean_word and clean_word not in unique_words:
        unique_words.append(clean_word)

print("Список уникальных слов:", unique_words)
