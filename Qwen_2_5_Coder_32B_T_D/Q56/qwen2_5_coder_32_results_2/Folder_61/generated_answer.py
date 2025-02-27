def all_substring_of_size_n(s):
    result = set()
    l = len(s)
    for i in range(l - 38):
        substring = s[i:i + 39]
        if len(set(substring)) == 39:
            result.add(substring)
    return list(result)