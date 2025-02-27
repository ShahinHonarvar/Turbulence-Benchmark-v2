def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 75 + 1):
        substr = s[i:i + 75]
        if len(set(substr)) == 75:
            result.add(substr)
    return list(result)