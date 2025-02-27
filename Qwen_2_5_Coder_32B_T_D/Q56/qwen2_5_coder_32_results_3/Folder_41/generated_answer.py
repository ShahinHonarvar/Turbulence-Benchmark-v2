def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 74 + 1):
        substring = s[i:i + 74]
        if len(set(substring)) == 74:
            result.add(substring)
    return list(result)