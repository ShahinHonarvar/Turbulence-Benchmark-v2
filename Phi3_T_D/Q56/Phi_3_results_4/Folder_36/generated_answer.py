def all_substring_of_size_n(s):
    result = set()
    n = len(s)
    target_length = 146
    if len(s) < target_length:
        return list(result)
    seen = set()
    for i in range(n - target_length + 1):
        substring = s[i:i + target_length]
        if len(set(substring)) == target_length and substring not in seen:
            result.add(substring)
            seen.add(substring)
    return list(result)