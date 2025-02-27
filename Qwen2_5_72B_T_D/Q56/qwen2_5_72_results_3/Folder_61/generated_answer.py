def all_substring_of_size_n(s):
    substrings = []
    n = 39
    for i in range(len(s) - n + 1):
        if len(set(s[i:i + n])) == n:
            substrings.append(s[i:i + n])
    return substrings