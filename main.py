from stats import count_word, count_characters, order
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    fpath = sys.argv[1]
    book = get_book_text(fpath)
    num_words = count_word(book)
    character_dict = count_characters(book)
    ##PRINT REPORT##
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {fpath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")  
    sorted_list = order(character_dict)
    for i in range(0, len(sorted_list)-1):
        print(f"{sorted_list[i]["char"]}: {sorted_list[i]["count"]}")
    print("============= END ===============")
    return None

main()
