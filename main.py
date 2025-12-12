from stats import count_word, count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    fpath = "books/frankenstein.txt"
    book = get_book_text(fpath)
    num_words = count_word(book)
    character_dict = count_characters(book)
    print(f"Found {num_words} total words")
    print(character_dict)
    return None

main()
