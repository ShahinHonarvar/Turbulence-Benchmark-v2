def all_substring_of_size_n(s):
    substrings = set()
    n = 61
    for start in range(len(s) - n + 1):
        substring = s[start:start + n]
        if len(set(substring)) == n:
            substrings.add(substring)
    return list(substrings)