def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 21):
        sub = s[i:i + 22]
        if len(set(sub)) == 22:
            result.add(sub)
    return list(result)