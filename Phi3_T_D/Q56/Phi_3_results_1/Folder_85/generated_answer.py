def all_substring_of_size_n(s):
    n = 14
    ans_set = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            ans_set.add(substring)
    return list(ans_set)