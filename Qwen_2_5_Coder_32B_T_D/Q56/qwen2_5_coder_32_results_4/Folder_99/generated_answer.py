def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 109):
        sub = s[i:i + 110]
        if len(set(sub)) == 110:
            result.add(sub)
    return list(result)