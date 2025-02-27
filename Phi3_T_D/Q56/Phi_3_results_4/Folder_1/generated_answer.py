def all_substring_of_size_n(s):
    subs = set()
    for i in range(len(s) - 23):
        temp = set(s[i:i + 24])
        if len(temp) == 24:
            subs.add(str(temp))
    return list(subs)