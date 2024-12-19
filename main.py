def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = convert_chars_dict(chars_dict)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item["char"]}' character was found {item["num"]} times")
    print("--- End report ---")
    

def sort_on(d):
    return d["num"]

def convert_chars_dict(dict):
    chars_list = []
    for ch in dict:
        chars_list.append({"char":ch, "num": dict[ch]})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1    
    return chars


def count_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()