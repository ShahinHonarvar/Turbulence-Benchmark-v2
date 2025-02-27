def all_substring_of_size_n(s):
    subs = []
    for i in range(len(s) - 43):
        sub = s[i:i + 44]
        if len(set(sub)) == 44:
            subs.append(sub)
    return subs