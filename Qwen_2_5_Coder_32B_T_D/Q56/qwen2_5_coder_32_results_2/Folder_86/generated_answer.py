def all_substring_of_size_n(s):
    result = set()
    if len(s) < 143:
        return []
    for i in range(len(s) - 142):
        substring = s[i:i + 143]
        if len(set(substring)) == 143:
            result.add(substring)
    return list(result)