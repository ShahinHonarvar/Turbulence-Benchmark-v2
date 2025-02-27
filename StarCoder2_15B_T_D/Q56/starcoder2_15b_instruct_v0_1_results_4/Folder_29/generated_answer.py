def all_substring_of_size_n(text):
    substrings = set()
    for i in range(len(text) - 94):
        substring = text[i:i + 95]
        if len(set(substring)) == 95:
            substrings.add(substring)
    return list(substrings)