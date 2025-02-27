def all_substring_of_size_n(s):
    n = 19
    substrings = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(substring) == n and len(set(substring)) == n:
            substrings.add(substring)
    return list(substrings)