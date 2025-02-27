def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 21):
        subst = s[i:i + 22]
        if len(set(subst)) == 22:
            result.add(subst)
    return list(result)