def num_words(contents):
    words = len(contents.split())
    return words

def num_chars(contents):
    char_dict = {}
    contents_lower = contents.lower()

    for char in contents_lower:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict