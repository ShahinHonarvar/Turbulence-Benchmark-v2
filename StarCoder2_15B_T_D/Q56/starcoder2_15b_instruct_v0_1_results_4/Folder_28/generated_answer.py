import itertools

def all_substring_of_size_n(text):
    substrings = []
    for i in range(len(text) - 3):
        substring = text[i:i + 4]
        if len(set(substring)) == 4:
            substrings.append(substring)
    return substrings