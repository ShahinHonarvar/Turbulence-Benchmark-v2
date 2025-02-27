def all_substring_of_size_n(s):
    length = len(s)
    result = set()
    if length < 6:
        return list(result)
    for i in range(length - 5):
        substring = s[i:i + 6]
        if len(set(substring)) == 6:
            result.add(substring)
    return list(result)