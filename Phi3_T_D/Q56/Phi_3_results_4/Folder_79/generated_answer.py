def all_substring_of_size_n(s):
    n = 61
    length = len(s)
    if length < n:
        return []
    substrings = set()
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            substrings.add(substring)
    return list(substrings)