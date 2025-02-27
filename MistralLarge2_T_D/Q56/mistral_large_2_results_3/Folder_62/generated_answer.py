def all_substring_of_size_n(s):
    result = set()
    length = len(s)
    for i in range(length - 31):
        substring = s[i:i + 32]
        if len(set(substring)) == 32:
            result.add(substring)
    return list(result)