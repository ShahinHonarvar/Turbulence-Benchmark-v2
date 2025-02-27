def all_substring_of_size_n(s):
    substrings = set()
    len_dif = len(s) - 19
    for i in range(len_dif + 1):
        sub = s[i:i + 19]
        if len(set(sub)) == 19:
            substrings.add(sub)
    return list(substrings)