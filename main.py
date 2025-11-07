from stats import get_num_words
from stats import get_chars
from stats import build_report

frankenstein = "books/frankenstein.txt"

def get_book_text(file):
    with open(file) as f:
        return f.read()

def get_wc_ch(book):
    book_string = get_book_text(book)
    wc = get_num_words(book_string) # Passes string from get_book_text to get_num_words
    
    return wc

def get_ch(book):
    book_string = get_book_text(book)
    ch = get_chars(book_string)

    return ch

def get_report(book):
    book_string = get_book_text(book)
    report = build_report(book_string)

    return report

def format_output(book, wc, report):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book}...")
    print(f"----------- Word Count ----------\nFound {wc} total words")
    print("--------- Character Count -------")
    
    for character in report:
        print(f"{character["char"]}: {character["num"]}")

#get_wc_ch(frankenstein)
format_output(frankenstein, get_wc_ch(frankenstein), get_report(frankenstein))
