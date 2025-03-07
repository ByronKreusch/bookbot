def get_num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    character_dict = {}
    words = text.lower()
    for character in words:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def sort_on(dict):
    return dict["value"]

def sort_dict(char_count):
    sorted_dict = []
    for key in char_count:
        if key.isalpha():
            sorted_dict.append({ 'char': key, 'value': char_count[key] })
    sorted_dict.sort(reverse=True, key=sort_on)
    return sorted_dict