import sys
from stats import get_word_count, get_character_count, char_sorter
def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content


def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    sorted_characters = char_sorter(character_count)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")
    for x in sorted_characters:
        if not x["char"].isalpha():
            continue
        print(f"{x["char"]}: {x["nums"]}")
     
    print(f"============= END ===============")


main()



