def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 90):
        substr = s[i:i + 91]
        if len(set(substr)) == 91:
            result.add(substr)
    return list(result)