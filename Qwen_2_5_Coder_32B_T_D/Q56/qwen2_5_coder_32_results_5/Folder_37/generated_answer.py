def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 64):
        substr = s[i:i + 65]
        if len(set(substr)) == 65:
            result.add(substr)
    return list(result)