import sys
from stats import word_count, character_count, sort_chars

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents


def main():

        book_path = sys.argv[1]

            # Get the contents of the book
        text = get_book_text(book_path)

            # Count words in the text
        word_total = word_count(text)

            # Count characters in the text
        char_count = character_count(text)



        sorted_chars = sort_chars(char_count)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_total} total words")
        print("--------- Character Count -------")

        for char_dict in sorted_chars:
            char = char_dict["char"]
            count = char_dict["num"]

            if char.isalpha():
                print(f"{char}: {count}")

        print("============= END ===============")


main()
