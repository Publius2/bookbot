def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = wordcount(text)
    print(f"{num_words} words in book")
    character_count = count_characters(text)
    for x in character_count:
        print(f"{x} : {character_count[x]}")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    characterdict = dict()
    for x in text:
       characterdict[x.lower()] = characterdict.get(x.lower(), 0) + 1 
    return characterdict

def wordcount(text):
    words = text.split()
    return len(words)
    

main()