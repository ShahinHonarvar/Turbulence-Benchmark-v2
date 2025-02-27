def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 29):
        substring = s[i:i + 30]
        if len(set(substring)) == 30:
            result.add(substring)
    return list(result)