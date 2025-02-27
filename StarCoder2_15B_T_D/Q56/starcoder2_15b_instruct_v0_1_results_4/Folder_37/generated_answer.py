def all_substring_of_size_n(text):
    substrings = set()
    n = 65
    for i in range(len(text) - n + 1):
        substring = text[i:i + n]
        if len(set(substring)) == n:
            substrings.add(substring)
    return list(substrings)