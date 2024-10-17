import sys

def check_input(dictionary):
    with open(dictionary, 'r', encoding='utf-8') as file:
        words = set(line.strip() for line in file if line.strip())
    return words

ordinal = lambda n: f"{n}{'th' if 10 <= n % 100 <= 20 else {1:'st', 2:'nd', 3:'rd'}.get(n % 10, 'th')}"

def check_spelling(word, cleaned_dictionary):
    with open(word, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            words = line.strip().split()
            print("words:", words)
            for word_position, incorrect_word in enumerate(words, start=1):
                if incorrect_word not in cleaned_dictionary:
                    print(f"line {line_number}, {ordinal(word_position)} word {incorrect_word} is incorrect.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dzongkha_spell_checker.py dzo.txt")
        sys.exit(1)

    word = sys.argv[1]
    dictionary = 'cleaned_dictionary.txt'
    dzongkha_dictionary = check_input(dictionary)

    check_spelling(word, dzongkha_dictionary)