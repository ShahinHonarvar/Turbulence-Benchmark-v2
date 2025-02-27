def all_substring_of_size_n(s):
    n = 30
    substrings = []
    for i in range(len(s) - n + 1):
        window = s[i:i + n]
        if len(set(window)) == n:
            substrings.append(window)
    return substrings