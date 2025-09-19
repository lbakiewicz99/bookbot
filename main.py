from stats import get_num_words, get_num_letters, sort_dictionary
import sys

def get_book_text(filepath):
    with open(filepath) as temp:
        file_contents = temp.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    numb_dictionary = sort_dictionary(get_num_letters(text))
    for item in numb_dictionary:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()