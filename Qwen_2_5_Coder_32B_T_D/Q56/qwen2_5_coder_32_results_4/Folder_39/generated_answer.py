def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 93):
        substr = s[i:i + 94]
        if len(set(substr)) == 94:
            result.add(substr)
    return list(result)