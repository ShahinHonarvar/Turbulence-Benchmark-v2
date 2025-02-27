def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 24):
        substring = s[i:i + 25]
        if len(set(substring)) == 25:
            result.add(substring)
    return list(result)