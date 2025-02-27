def all_substring_of_size_n(s):
    substr_set = set()
    n = 42
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            substr_set.add(substring)
    return list(substr_set)