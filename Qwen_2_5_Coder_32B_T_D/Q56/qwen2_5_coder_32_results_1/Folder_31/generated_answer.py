def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 45):
        substr = s[i:i + 46]
        if len(set(substr)) == 46:
            result.add(substr)
    return list(result)