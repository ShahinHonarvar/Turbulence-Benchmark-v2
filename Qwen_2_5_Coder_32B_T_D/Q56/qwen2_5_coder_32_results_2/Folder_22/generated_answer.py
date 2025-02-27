def all_substring_of_size_n(s):
    result = set()
    l = len(s)
    for i in range(l - 21):
        substring = s[i:i + 22]
        if len(set(substring)) == 22:
            result.add(substring)
    return list(result)