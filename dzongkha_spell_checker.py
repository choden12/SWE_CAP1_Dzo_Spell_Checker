import sys

#function to load the dictionary from a file and return a set of words
def check_input(dictionary):
    with open(dictionary, 'r', encoding='utf-8') as file:#open dictionary file
        words = set(line.strip() for line in file if line.strip())
    return words

#lambda function to get the ordinal suffix for number
ordinal = lambda n: f"{n}{'th' if 10 <= n % 100 <= 20 else {1:'st', 2:'nd', 3:'rd'}.get(n % 10, 'th')}"

#check the spelling of words from the input file
def check_spelling(word, cleaned_dictionary):
    with open(word, 'r', encoding='utf-8') as file:#open the input file containing words to check
        for line_number, line in enumerate(file, start=1):
            words = line.strip().split()#split the line into individual words 
            print("words:", words)
            for word_position, incorrect_word in enumerate(words, start=1):
                if incorrect_word not in cleaned_dictionary:#if the word is not in the dictionary its incorrect
                    #print error message with line number
                    print(f"line {line_number}, {ordinal(word_position)} word {incorrect_word} is incorrect.")

#Main block to excute the script when called from command line
if __name__ == "__main__":
    #check if correct number of command line is provided 
    if len(sys.argv) != 2:
        print("Usage: python dzongkha_spell_checker.py dzo.txt")
        sys.exit(1)

#get input file from command line argument
    word = sys.argv[1]
    dictionary = 'cleaned_dictionary.txt'
    dzongkha_dictionary = check_input(dictionary)
#called the spell checking function with input file and dictionary
    check_spelling(word, dzongkha_dictionary)