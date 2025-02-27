def all_substring_of_size_n(s):
    n = 97
    if n > len(s):
        return []
    substr_set = set()
    for i in range(len(s) - n + 1):
        if len(set(s[i:i + n])) == n:
            substr_set.add(s[i:i + n])
    return list(substr_set)