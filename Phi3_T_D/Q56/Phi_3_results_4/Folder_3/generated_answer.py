def all_substring_of_size_n(s):
    result = set()
    str_len = len(s)
    if str_len < 93:
        return list(result)
    for i in range(str_len - 92):
        if len(set(s[i:i + 93])) == 93:
            result.add(s[i:i + 93])
    return list(result)