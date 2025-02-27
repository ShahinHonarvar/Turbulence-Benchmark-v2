def all_substring_of_size_n(s):
    n = 90
    substrings = []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings