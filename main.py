import sys
from stats import calc_words, calc_symbols

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def make_map(symbols):
    result = []
    for key in symbols:
        result.append({"char": key, "num": symbols[key]})
    return result

def sort_on(item):
    return item['num']

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    words_count = calc_words(text)
    char_count = make_map(calc_symbols(text))
    char_count.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")

    for char in char_count:
        ch = char['char']
        if ch.isalpha():
            print(f"{ch}: {char['num']}")

    print("============= END ===============")


main()