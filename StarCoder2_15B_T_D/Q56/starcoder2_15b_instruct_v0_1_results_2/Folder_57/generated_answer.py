def all_substring_of_size_n(text):
    substrings = []
    n = 60
    for i in range(len(text) - n + 1):
        substring = text[i:i + n]
        if len(set(substring)) == n:
            substrings.append(substring)
    return substrings