def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 66):
        sub = s[i:i + 67]
        if len(set(sub)) == 67:
            result.add(sub)
    return list(result)