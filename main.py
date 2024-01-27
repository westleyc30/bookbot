import sys


def main() -> int:
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    print(word_count(text))
    letters = letter_count(text)
    letter_list = list(letters)
    sorted(letter_list, key=lambda letter: letters[letter])
    print(sorted_letters(letters))


def get_book_text(path):
    with open(path) as f:
        return f.read()


def word_count(text):
    words = text.split()
    return len(words)


def letter_count(text):
    letters = {}
    for letter in text:
        letter = letter.lower()
        if letter in letters:
            letters[letter] += 1
        else:
            if letter.isalpha():
                letters[letter] = 1
    return letters


def sort_on(d):
    '''
    helper function for sort()
    when put into key allows a list to be
    sorted by the dictionary key "num"
    '''
    return d["num"]


def sorted_letters(letters):
    sorted = []
    for letter in letters:
        sorted.append({"char": letter, "num": letters[letter]})
    sorted.sort(key=sort_on, reverse=True) # use the sort_on helper function
    return sorted


if __name__ == '__main__':
    sys.exit(main())
