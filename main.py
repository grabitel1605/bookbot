from stats import num_words, num_chars
import sys

#file = "books/frankenstein.txt"

def get_book_stats(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents



def main():
    if len(sys.argv) == 2:
        file = sys.argv[1]
        contents = str(get_book_stats(file))
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file}...")
        wordcount = num_words(contents)          
        print("----------- Word Count ----------")
        print(f"Found {wordcount} total words")
        charcount = num_chars(contents)
        print("--------- Character Count -------")
        for key, value in sorted(charcount.items()):
            if str(key).isalpha() and str(value).isalpha():
                print(f"{key}: {value}")
            elif str(key).isalpha() and not str(value).isalpha():
                print(f"{key}: {value}")
            elif not str(key).isalpha() and str(value).isalpha():
                print(f"{key}: {value}")
            else:
                continue
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)



if __name__ == "__main__":
    main()