def all_substring_of_size_n(s):
    subs = set()
    for i in range(len(s) - 26):
        sub = s[i:i + 27]
        if len(set(sub)) == 27:
            subs.add(sub)
    return list(subs)