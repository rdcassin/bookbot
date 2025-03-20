import sys
from stats import get_num_words, get_num_letters, sort_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    source = sys.argv[1]

    def print_results(statistics, total_words, source):

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {source}...")
        print("----------- Word Count ----------")
        print(f"Found {total_words} total words")
        print("--------- Character Count -------")

        for stat in statistics:
            print(f"{stat["character"]}: {stat["count"]}")

        print("============= END ===============")

    def get_book_text(filepath):
        with open(filepath) as f:
            file_contents = f.read()
        
        return file_contents

    def main():
        book_text = get_book_text(f"./{source}")
        word_count = get_num_words(book_text)
        num_letters = get_num_letters(book_text)
        result = sort_list(num_letters)
        print_results(result, word_count, source)

    main()