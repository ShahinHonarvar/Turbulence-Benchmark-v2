def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 19):
        substr = s[i:i + 20]
        if len(set(substr)) == 20:
            result.add(substr)
    return list(result)