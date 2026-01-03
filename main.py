from stats import get_word_count, get_char_count, sort_on, create_list
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    file_contents = get_books_text(filepath)
    print(file_contents)
    word_count = get_word_count(file_contents)
    print(f"Found {word_count} total words")
    char_count = get_char_count(file_contents)
    print(char_count)
    char_count_to_list = create_list(char_count)
    char_count_to_list.sort(key=sort_on, reverse=True)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found " + str(word_count) + " total words")
    print("--------- Character Count -------")
    for item in char_count_to_list:
        print(f"{item['char']}: {item['nums']}")
    print("============= END ===============")

def get_books_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
        




main()