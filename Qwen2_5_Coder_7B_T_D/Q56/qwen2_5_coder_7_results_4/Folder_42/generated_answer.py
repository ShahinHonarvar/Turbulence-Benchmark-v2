def all_substring_of_size_n(s):
    n = len(s)
    result = set()
    for i in range(n - 44):
        substring = s[i:i + 45]
        if len(set(substring)) == 45:
            result.add(substring)
    return list(result)