def all_substring_of_size_n(text):
    substrings = set()
    for i in range(len(text) - 29):
        substring = text[i:i + 30]
        if len(set(substring)) == 30:
            substrings.add(substring)
    return list(substrings)