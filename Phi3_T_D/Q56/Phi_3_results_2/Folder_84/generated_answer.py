def all_substring_of_size_n(s):
    n = 114
    substrings = set()
    if len(s) < n:
        return list(substrings)
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            substrings.add(substring)
    return list(substrings)