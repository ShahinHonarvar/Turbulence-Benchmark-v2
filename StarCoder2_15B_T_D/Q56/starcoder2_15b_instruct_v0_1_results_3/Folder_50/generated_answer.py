def all_substring_of_size_n(text):
    substrings = []
    for i in range(len(text) - 10):
        substring = text[i:i + 11]
        if len(set(substring)) == len(substring):
            substrings.append(substring)
    return substrings