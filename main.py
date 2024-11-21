def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = wordcount(text)
    character_count = count_characters(text)

    print("===================Text Report======================")
    print(f"{num_words} words in book")
    print("------------------------Character Analysis-------------------------")
    for x in sorted(character_count, reverse=True, key=character_count.get):
        if x.isalpha(): print(f"{x} occurs {character_count[x]} times")

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