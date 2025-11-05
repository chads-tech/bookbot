from stats import get_num_words

frankenstein = "books/frankenstein.txt"

def get_book_text(file):
    with open(file) as f:
        return f.read()

def main():
    get_num_words(get_book_text(frankenstein)) # Passes string from get_book_text to get_num_words

main()
