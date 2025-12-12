def count_word(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_dict={}
    for ch in text:
        if ch.lower() in char_dict:
            char_dict[ch.lower()] += 1
        else: char_dict[ch.lower()] = 1
    return char_dict