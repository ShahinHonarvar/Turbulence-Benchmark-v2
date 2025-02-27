def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 16):
        substr = s[i:i + 17]
        if len(set(substr)) == 17:
            result.add(substr)
    return list(result)