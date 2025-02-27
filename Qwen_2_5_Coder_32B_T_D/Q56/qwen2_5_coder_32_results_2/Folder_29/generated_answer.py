def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 95 + 1):
        substring = s[i:i + 95]
        if len(set(substring)) == 95:
            result.add(substring)
    return list(result)