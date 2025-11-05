def get_num_words(book):
    num_words = 0
    word_list = book.split()
    
    for words in word_list:
        num_words += 1

    print(f"Found {num_words} total words")
