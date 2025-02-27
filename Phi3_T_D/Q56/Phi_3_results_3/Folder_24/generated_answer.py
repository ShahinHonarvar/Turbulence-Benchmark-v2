def all_substring_of_size_n(s):
    n = 52
    substrings = set()
    for i in range(len(s) - n + 1):
        substring = ''.join(sorted(set(s[i:i + n])))
        if len(substring) == n:
            substrings.add(substring)
    return list(substrings)