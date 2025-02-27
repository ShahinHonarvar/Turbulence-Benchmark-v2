def all_substring_of_size_n(s):
    substrings = set()
    n = 60
    length = len(s)
    for i in range(length - n + 1):
        substr = s[i:i + n]
        if len(set(substr)) == n:
            substrings.add(substr)
    return list(substrings)