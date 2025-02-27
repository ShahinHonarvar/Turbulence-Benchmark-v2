def all_substring_of_size_n(s):
    length = 56
    result = set()
    for i in range(len(s) - length + 1):
        if len(set(s[i:i + length])) == length:
            result.add(s[i:i + length])
    return list(result)