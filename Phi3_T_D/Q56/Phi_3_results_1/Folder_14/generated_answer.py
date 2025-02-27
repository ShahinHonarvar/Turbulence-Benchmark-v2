def all_substring_of_size_n(s):
    substrings = set()
    n = 85
    for i in range(len(s) - n + 1):
        window = s[i:i + n]
        if len(set(window)) == n:
            substrings.add(window)
    return list(substrings)