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

def sort_on(d):
    return d["count"]

def order(char_dict):
    sorted = []
    for char in char_dict:
        if char.isalpha():
            sorted.append({"char": char, "count": char_dict[char]})
            sorted.sort(reverse=True, key=sort_on)
    return sorted