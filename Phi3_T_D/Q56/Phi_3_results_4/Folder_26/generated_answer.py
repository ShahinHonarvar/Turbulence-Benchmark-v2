def all_substring_of_size_n(s):
    n = 33
    seen = set()
    result = []
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if len(set(substr)) == n and substr not in seen:
            result.append(substr)
            seen.add(substr)
    return result