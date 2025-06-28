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

def sort_on(dict):
    return dict["num"]
    
def sort_dict(character_count):
    dict_list = []
    for k in character_count:
        k_dict = {"char":k, "num":character_count[k]}
        dict_list.append(k_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

   

   