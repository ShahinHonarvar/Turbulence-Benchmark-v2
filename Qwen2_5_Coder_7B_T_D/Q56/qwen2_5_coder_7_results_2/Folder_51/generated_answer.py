def all_substring_of_size_n(s):
    n = 96
    seen = set()
    result = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n and substring not in seen:
            seen.add(substring)
            result.add(substring)
    return list(result)