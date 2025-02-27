def all_substring_of_size_n(s):
    n = 142
    substrings = []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            substrings.append(substring)
    return substrings