def all_substring_of_size_n(s):
    size = 106
    result = set()
    if size > len(s):
        return []
    for i in range(len(s) - size + 1):
        substring = s[i:i + size]
        if len(set(substring)) == size:
            result.add(substring)
    return list(result)