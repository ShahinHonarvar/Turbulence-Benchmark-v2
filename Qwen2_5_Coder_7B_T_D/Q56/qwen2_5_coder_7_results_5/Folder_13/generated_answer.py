def all_substring_of_size_n(s):
    n = 53
    substring_set = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(substring) == len(set(substring)):
            substring_set.add(substring)
    return list(substring_set)