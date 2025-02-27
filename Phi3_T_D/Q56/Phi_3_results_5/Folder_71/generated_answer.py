def all_substring_of_size_n(s):
    result = set()
    sub_len = 17
    for i in range(len(s) - sub_len + 1):
        substring = s[i:i + sub_len]
        if len(set(substring)) == sub_len:
            result.add(substring)
    return list(result)