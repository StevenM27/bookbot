from stats import count_words, count_characters

def get_book_text(filepath):

    contents = None

    with open(filepath) as f:
        contents = f.read()

    return contents


def main():
    
    content = get_book_text("./books/frankenstein.txt")
    num_words = count_words(content)

    print(f"{num_words} words found in the document")

    char_dict = count_characters(content)

    print(char_dict)


main()