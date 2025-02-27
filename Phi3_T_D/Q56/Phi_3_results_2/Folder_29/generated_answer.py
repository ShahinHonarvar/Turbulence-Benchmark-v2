def all_substring_of_size_n(s):
    subs = set()
    for i in range(len(s) - 94):
        sub = s[i:i + 95]
        if len(set(sub)) == 95:
            subs.add(sub)
    return list(subs)