def all_substring_of_size_n(s):
    length = 34
    result = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if len(set(substring)) == length:
            result.add(substring)
    return list(result)