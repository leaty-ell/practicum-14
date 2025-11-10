def count_hole_letters(word):
    """Count letters with holes in a word.
    Args:
        word: Input word to analyze.
    Returns:
        Number of letters with holes.
    """
    hole_letters = {'a', 'b', 'd', 'e', 'g', 'o', 'p', 'q'}
    count = 0
    for letter in word:
        if letter in hole_letters:
            count += 1
    return count


def analyze_text():
    """
    Analyze text for letters with holes.
    Counts hole letters, non-hole letters, and finds words with multiple hole letters.
    """
    text = input(Введите строку из слов в нижнем регистре: ")
    words = text.split()

    hole_count = 0
    no_hole_count = 0
    all_letters = set('abcdefghijklmnopqrstuvwxyz')
    hole_letters = {'a', 'b', 'd', 'e', 'g', 'o', 'p', 'q'}

    for word in words:
        for letter in word:
            if letter in hole_letters:
                hole_count += 1
            elif letter in all_letters:
                no_hole_count += 1

    words_with_holes = []
    for word in words:
        if count_hole_letters(word) >= 2:
            words_with_holes.append(word)

    print(f"Букв с отверстиями {hole_count}")
    print(f"Букв без отверстий: {no_hole_count}")
    print(f"Слова с двумя и более буквами с отверстиями: {words_with_holes}")


def main():
    """
    Run text analysis.
    """
    analyze_text()


if __name__ == "__main__":
    main()
