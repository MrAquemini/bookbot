def get_word_count(text):
    return len(text.split())

def get_character_count(text):
    letter_count = {}
    lc_text = text.lower()
    for letter in lc_text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    return letter_count    

def sort_on(dict):
    return dict["nums"]

def char_sorter(character_count):
    dict_list = []
    for char in character_count:
        dict_list.append({"char":char,
         "nums":character_count[char]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

