print("Введите текст :")

all_text = ""
while True:
    line = input()
    if line == "":
        break
    all_text = all_text + line + " "

signs = ".,!?;:()\"'-"

clean_text = ""
for char in all_text:
    if char not in signs:
        clean_text = clean_text + char

clean_text = clean_text.lower()
words = clean_text.split()

word_count = {}
word_order = []

for word in words:
    if word not in word_count:
        word_count[word] = 0
        word_order.append(word)
    word_count[word] = word_count[word] + 1

sorted_words = []
for word in word_order:
    sorted_words.append((word_count[word], word))


sorted_words.sort()
sorted_words = sorted_words[::-1]

print("\nСлова по частоте (от самого частого к самому редкому):")
for count, word in sorted_words:
    print(word)
