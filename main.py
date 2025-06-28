file_path = "books/frankenstein.txt"

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content


def main():
    from stats import get_word_count, get_character_count
    text = get_book_text(file_path)
    get_word_count(text)
    get_character_count(text)
main()

