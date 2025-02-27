def all_substring_of_size_n(text):
    n = 64
    all_substrings = []
    for i in range(len(text) - n + 1):
        substring = text[i:i + n]
        if len(set(substring)) == n:
            all_substrings.append(substring)
    return all_substrings