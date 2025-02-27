def all_substring_of_size_n(s):
    l = len(s)
    result = set()
    for i in range(l - 92):
        substring = s[i:i + 93]
        if len(set(substring)) == 93:
            result.add(substring)
    return list(result)