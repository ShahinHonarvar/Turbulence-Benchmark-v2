def all_substring_of_size_n(s):
    n = len(s)
    result = set()
    for i in range(n - 42):
        substring = s[i:i + 43]
        if len(set(substring)) == 43:
            result.add(substring)
    return list(result)