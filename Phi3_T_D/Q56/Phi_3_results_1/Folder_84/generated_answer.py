def all_substring_of_size_n(s):
    n = 114
    return_list = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            return_list.add(substring)
    return list(return_list)