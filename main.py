from stats import get_num_words
from stats import get_chars

frankenstein = "books/frankenstein.txt"

def get_book_text(file):
    with open(file) as f:
        return f.read()

def get_wc_ch(book):
    book_string = get_book_text(book)
    wc = get_num_words(book_string) # Passes string from get_book_text to get_num_words
    ch = get_chars(book_string)
    
    print(wc)
    print(ch)

get_wc_ch(frankenstein)
