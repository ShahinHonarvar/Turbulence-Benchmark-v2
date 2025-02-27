def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 40):
        substr = s[i:i + 41]
        if len(set(substr)) == 41:
            result.add(substr)
    return list(result)