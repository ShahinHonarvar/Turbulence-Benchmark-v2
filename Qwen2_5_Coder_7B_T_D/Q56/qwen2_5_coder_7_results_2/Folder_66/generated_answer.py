def all_substring_of_size_n(s):
    n = len(s)
    if n < 26:
        return []
    substrings = set()
    for i in range(n - 25):
        substring = s[i:i + 26]
        if len(set(substring)) == 26:
            substrings.add(substring)
    return list(substrings)