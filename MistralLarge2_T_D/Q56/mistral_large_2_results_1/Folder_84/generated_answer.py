def all_substring_of_size_n(s):
    n = 114
    substrings = set()
    length = len(s)
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            substrings.add(substring)
    return list(substrings)