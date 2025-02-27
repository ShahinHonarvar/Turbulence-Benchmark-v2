def all_substring_of_size_n(s):
    n = 42
    seen = set()
    result = []
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if len(set(substr)) == n and substr not in seen:
            seen.add(substr)
            result.append(substr)
    return result