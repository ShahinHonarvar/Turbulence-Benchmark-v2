def all_substring_of_size_n(s):
    length = len(s)
    n = 96
    substrings_set = set()
    for i in range(length):
        for j in range(i + 1, length + 1):
            substring = s[i:j]
            if len(substring) == n and len(set(substring)) == n:
                substrings_set.add(substring)
    return list(substrings_set)