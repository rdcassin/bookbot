def get_num_words(text):
    num_words = len(text.split())
    return num_words

def get_num_letters(text):
    text_list = text.lower().split()
    letter_stats = {}

    for word in text_list:
        for letter in word:
            if letter in letter_stats:
                letter_stats[letter] += 1
            else:
                letter_stats[letter] = 1

    return letter_stats

def sort_list(dict):
    sorted_list = []

    for character in dict:
        if character.isalpha() == True:
            count = dict[character]
            sorted_list.append({"character": character, "count": count})

    sorted_list.sort(reverse=True, key=sort_method)
    
    return sorted_list

def sort_method(dict):
    return dict["count"]