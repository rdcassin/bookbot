from stats import get_num_letters
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    get_num_letters(file_contents)

def main():
    get_book_text("./books/frankenstein.txt")

main()