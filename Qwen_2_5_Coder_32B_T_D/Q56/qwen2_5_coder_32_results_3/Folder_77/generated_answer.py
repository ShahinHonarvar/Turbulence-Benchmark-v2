def all_substring_of_size_n(s):
    l = len(s)
    result = set()
    for i in range(l - 143):
        if len(set(s[i:i + 144])) == 144:
            result.add(s[i:i + 144])
    return list(result)