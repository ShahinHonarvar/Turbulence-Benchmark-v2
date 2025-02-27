def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 92):
        substr = s[i:i + 93]
        if len(set(substr)) == 93:
            result.add(substr)
    return list(result)