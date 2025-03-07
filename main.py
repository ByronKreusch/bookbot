import sys

from stats import get_num_words, character_count, sort_dict

def main():

 # Check if the correct number of arguments were provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # Use the provided filepath instead of the hardcoded one
    book_path = sys.argv[1]


    #book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = character_count(text)
    new_sorted_list = sort_dict(char_count)

    #print(f"{num_words} words found in the document")
    #print(char_count)
    #print(new_sorted_list)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for char in new_sorted_list:
       print(f"{char['char']}: {char['value']}")
    print(f"============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()