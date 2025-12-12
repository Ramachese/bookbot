def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def count_word(text):
    words = text.split()
    return len(words)

def main():
    fpath = "books/frankenstein.txt"
    book = get_book_text(fpath)
    num_words = count_word(book)
    print(f"Found {num_words} total words")
    return None

main()
