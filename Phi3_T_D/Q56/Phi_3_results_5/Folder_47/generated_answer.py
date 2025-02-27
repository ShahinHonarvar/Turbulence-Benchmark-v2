def all_substring_of_size_n(s):
    result = set()
    n = len(s)
    if n < 91:
        return list(result)
    for i in range(n - 90):
        if len(set(s[i:i + 91])) == 91:
            result.add(s[i:i + 91])
    return list(result)