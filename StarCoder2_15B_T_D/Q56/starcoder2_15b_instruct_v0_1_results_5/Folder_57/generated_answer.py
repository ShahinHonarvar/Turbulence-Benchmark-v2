def all_substring_of_size_n(text):
    substrings = set()
    for i in range(len(text) - 59):
        substring = text[i:i + 60]
        if len(set(substring)) == 60:
            substrings.add(substring)
    return list(substrings)