def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 49):
        substr = s[i:i + 50]
        if len(set(substr)) == 50:
            result.add(substr)
    return list(result)