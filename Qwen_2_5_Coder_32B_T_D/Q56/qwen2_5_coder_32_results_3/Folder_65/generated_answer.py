def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 80):
        sub = s[i:i + 81]
        if len(set(sub)) == 81:
            result.add(sub)
    return list(result)