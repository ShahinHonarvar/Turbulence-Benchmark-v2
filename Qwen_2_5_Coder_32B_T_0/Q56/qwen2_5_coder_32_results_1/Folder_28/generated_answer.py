def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 43):
        substring = s[i:i + 44]
        if len(set(substring)) == 44:
            result.add(substring)
    return list(result)