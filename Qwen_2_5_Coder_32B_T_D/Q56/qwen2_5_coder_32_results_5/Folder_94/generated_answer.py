def all_substring_of_size_n(s):
    l = len(s)
    result = set()
    for i in range(l - 69):
        sub = s[i:i + 70]
        if len(set(sub)) == 70:
            result.add(sub)
    return list(result)