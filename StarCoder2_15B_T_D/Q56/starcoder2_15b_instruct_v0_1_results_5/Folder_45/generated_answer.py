def all_substring_of_size_n(text):
    n = 29
    substrings = []
    for i in range(len(text) - n + 1):
        substring = text[i:i + n]
        if len(set(substring)) == n:
            substrings.append(substring)
    return substrings