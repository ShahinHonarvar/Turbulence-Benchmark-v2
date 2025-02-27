def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 78):
        substr = s[i:i + 79]
        if len(set(substr)) == 79:
            result.add(substr)
    return list(result)