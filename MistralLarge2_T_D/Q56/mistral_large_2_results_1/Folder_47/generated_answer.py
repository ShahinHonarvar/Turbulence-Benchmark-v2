def all_substring_of_size_n(s):
    n = 91
    substrings = set()
    for i in range(len(s) - n + 1):
        sub_s = s[i:i + n]
        if len(set(sub_s)) == n:
            substrings.add(sub_s)
    return list(substrings)