def all_substring_of_size_n(text):
    substrings = []
    for i in range(len(text) - 55 + 1):
        if len(set(text[i:i + 55])) == 55:
            substrings.append(text[i:i + 55])
    return substrings