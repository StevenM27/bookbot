from stats import count_words, count_characters, sort_character_counts
import sys

def get_book_text(filepath):

    contents = None

    with open(filepath) as f:
        contents = f.read()

    return contents


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    
    content = get_book_text(filepath)
    num_words = count_words(content)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    char_dict = count_characters(content)
    sorted_chars = sort_character_counts(char_dict)

    print("--------- Character Count -------")

    for entry in sorted_chars:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")

    print("============= END ===============")



main()