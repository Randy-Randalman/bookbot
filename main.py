def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_dict = get_character_count(text)
    character_list = get_character_list(character_dict)
    character_list.sort(reverse=True, key=sort_on)
    create_report(book_path, num_words, character_list)


def create_report(path, num_words, character_list):
    print(f"\n--- Begin report of {path} ---")
    print(f"There are {num_words} words in this book.")
    for pair in character_list:
        print(f"The '{pair['char']}' character was found {pair['num']} times")
    print("--- End Report ---")


def get_character_list(dict):
    character_list = []
    for key, value in dict.items():
        if key.isalpha():
            char_dict = {"char": key, "num": value}
            character_list.append(char_dict)
    return character_list


def sort_on(dict):
    return dict["num"]


def get_character_count(text):
    character_count = {}
    for c in text:
        lowered = c.lower()
        if lowered in character_count:
            character_count[lowered] += 1
        else:
            character_count[lowered] = 1
    return character_count

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()