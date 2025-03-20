def get_num_words(text):
    text_list = text.split()
    num_words = 0

    for word in text_list:
        num_words += 1

    print(f"{num_words} words found in the document")

def get_num_letters(text):
    text_list = text.lower().split()
    letter_stats = {}

    for word in text_list:
        for letter in word:
            if letter in letter_stats:
                letter_stats[letter] += 1
            else:
                letter_stats[letter] = 1

    sort_stats(letter_stats)

def sort_stats(dict):
    return dict.sort(reverse=True, key=dict[""])