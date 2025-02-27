def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 7):
        substr = s[i:i + 8]
        if len(set(substr)) == 8:
            result.add(substr)
    return list(result)