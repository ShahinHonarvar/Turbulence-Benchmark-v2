def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 105):
        if len(set(s[i:i + 106])) == 106:
            result.add(s[i:i + 106])
    return list(result)