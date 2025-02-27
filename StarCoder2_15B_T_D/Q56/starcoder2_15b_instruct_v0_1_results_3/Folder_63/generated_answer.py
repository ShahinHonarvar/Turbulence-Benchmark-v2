def all_substring_of_size_n(text):
    substrings = []
    n = 19
    for i in range(len(text) - n + 1):
        substring = text[i:i + n]
        if len(substring) == n and len(set(substring)) == n:
            substrings.append(substring)
    return substrings