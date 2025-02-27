def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 64):
        sub = s[i:i + 75]
        if len(set(sub)) == 75:
            result.add(sub)
    return list(result)