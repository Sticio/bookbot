
def word_count(text):
    words = text.split()
    num_words = len(words)
    return num_words

def character_count(text):
    char_count = {}
    for char in text.lower():
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def sort_chars(char_count):
    char_list = []

    for char, count in char_count.items():
            char_dict = {"char": char, "num": count}
            char_list.append(char_dict)

    char_list.sort(reverse=True, key=lambda item: item["num"])

    return char_list
