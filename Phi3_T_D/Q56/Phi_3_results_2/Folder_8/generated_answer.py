def all_substring_of_size_n(s):
    length = 30
    n = len(s)
    if n < length:
        return []
    substrings = set()
    for i in range(n - length + 1):
        substring = s[i:i + length]
        if len(set(substring)) == length:
            substrings.add(substring)
    return list(substrings)