def all_substring_of_size_n(s):
    substrings = set()
    n = len(s)
    for i in range(n - 117 + 1):
        substring = s[i:i + 117]
        if len(set(substring)) == 117:
            substrings.add(substring)
    return list(substrings)