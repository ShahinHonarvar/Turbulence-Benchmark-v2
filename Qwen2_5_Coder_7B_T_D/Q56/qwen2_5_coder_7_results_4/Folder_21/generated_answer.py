def all_substring_of_size_n(s):
    n = len(s)
    if n < 106:
        return []
    substrings = set()
    for i in range(n - 105):
        substring = s[i:i + 106]
        if len(set(substring)) == 106:
            substrings.add(substring)
    return list(substrings)