def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 34):
        substr = s[i:i + 35]
        if len(set(substr)) == 35:
            result.add(substr)
    return list(result)