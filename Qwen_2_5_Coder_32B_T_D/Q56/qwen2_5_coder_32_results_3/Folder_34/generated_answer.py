def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 84 + 1):
        substring = s[i:i + 84]
        if len(set(substring)) == 84:
            result.add(substring)
    return list(result)