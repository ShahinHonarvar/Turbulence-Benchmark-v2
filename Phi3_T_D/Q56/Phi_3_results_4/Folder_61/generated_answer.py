def all_substring_of_size_n(s):
    n = 39
    length = len(s)
    substrings = set()
    if length < n:
        return list(substrings)
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            substrings.add(substring)
    return list(substrings)