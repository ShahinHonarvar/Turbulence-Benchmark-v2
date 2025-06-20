def all_substring_of_size_n(s):
    n = 117
    substrings = {}
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            substrings[substring] = 1
    return list(substrings.keys())