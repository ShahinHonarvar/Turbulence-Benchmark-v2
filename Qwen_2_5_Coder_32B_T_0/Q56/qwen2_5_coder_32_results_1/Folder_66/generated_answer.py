def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 25):
        substring = s[i:i + 26]
        if len(set(substring)) == 26:
            result.add(substring)
    return list(result)