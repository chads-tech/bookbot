#from main import get_wc_ch

def get_num_words(book):
    num_words = 0
    word_list = book.split()
    
    for words in word_list:
        num_words += 1

    return num_words
    #print(f"Found {num_words} total words")

def get_chars(book):
    characters = {}
    
    for character in book:
        character = character.lower() # Convert all characters to lowercase

        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1 

    return characters
    #print(characters)

def sort_by(index):
    #return index
    pass

def build_report(chars):
    new_counter = {}

    for letter in chars:
        ...

def test_function():
    testing_string = "A simple SET of mixed CHARacters for TEStING"

    wc = get_num_words(testing_string)
    ch = get_chars(testing_string)
    #report = build_report(get_chars(testing_string))
    return wc, ch

print(test_function())
