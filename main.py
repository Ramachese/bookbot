from stats import count_word, count_characters, order

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    fpath = "books/frankenstein.txt"
    book = get_book_text(fpath)
    num_words = count_word(book)
    character_dict = count_characters(book)
    ##PRINT REPORT##
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")  
    sorted_list = order(character_dict)
    for i in range(0, len(sorted_list)-1):
        print(f"{sorted_list[i]["char"]}: {sorted_list[i]["count"]}")
    print("============= END ===============")
    return None

main()
