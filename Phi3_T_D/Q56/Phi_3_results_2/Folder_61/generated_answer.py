def all_substring_of_size_n(s):
    subs = set()
    for i in range(len(s) - 38):
        sub = s[i:i + 39]
        if len(set(sub)) == 39:
            subs.add(sub)
    return list(subs)