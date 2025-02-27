def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 116):
        substr = s[i:i + 117]
        if len(set(substr)) == 117:
            result.add(substr)
    return list(result)