def all_substring_of_size_n(s):
    length = len(s)
    subs = set()
    for i in range(length):
        for j in range(i + 22, min(length, i + 23) + 1):
            substring = s[i:j]
            if len(substring) == 22 and len(set(substring)) == 22:
                subs.add(substring)
    return list(subs)