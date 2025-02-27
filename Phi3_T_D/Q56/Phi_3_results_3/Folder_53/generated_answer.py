def all_substring_of_size_n(s):
    n = len(s)
    if n < 25:
        return []
    substrings = set()
    for i in range(n - 24):
        substring = s[i:i + 25]
        if len(set(substring)) == 25:
            substrings.add(substring)
    return list(substrings)