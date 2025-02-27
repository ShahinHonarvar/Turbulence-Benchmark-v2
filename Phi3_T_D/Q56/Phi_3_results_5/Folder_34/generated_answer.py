def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 83):
        substr = s[i:i + 84]
        if len(set(substr)) == 84:
            result.add(substr)
    return list(result)