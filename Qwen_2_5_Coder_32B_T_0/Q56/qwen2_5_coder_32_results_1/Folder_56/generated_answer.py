def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 68):
        substring = s[i:i + 69]
        if len(set(substring)) == 69:
            result.add(substring)
    return list(result)