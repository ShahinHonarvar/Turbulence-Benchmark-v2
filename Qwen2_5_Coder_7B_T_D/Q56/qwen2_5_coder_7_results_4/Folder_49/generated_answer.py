def all_substring_of_size_n(s):
    n = 73
    result = []
    used = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(substring) == n and all((c not in used for c in substring)):
            result.append(substring)
            for c in substring:
                used.add(c)
    return result