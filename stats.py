def get_word_count(text):
    words = text.split()
    count = len(words)
    print(f"{count} words found in the document")

def get_character_count(text):
    letter_count = {}
    lc_text = text.lower()
    for letter in lc_text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    return letter_count    

def sort_on()

   