def all_substring_of_size_n(s):
    result = set()
    n = 55
    if n > len(s):
        return []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            result.add(substring)
    return list(result)