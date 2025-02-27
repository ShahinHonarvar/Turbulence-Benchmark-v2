def all_substring_of_size_n(s):
    if len(s) < 65:
        return []
    substr_set = set()
    for i in range(len(s) - 64):
        substr = s[i:i + 65]
        if len(set(substr)) == 65:
            substr_set.add(substr)
    return list(substr_set)