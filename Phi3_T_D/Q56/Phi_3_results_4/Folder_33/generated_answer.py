def all_substring_of_size_n(text):
    length = 105
    substrings = set()
    for i in range(len(text) - length + 1):
        substring = text[i:i + length]
        if len(set(substring)) == length:
            substrings.add(substring)
    return list(substrings)