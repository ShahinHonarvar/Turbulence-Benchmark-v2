def all_substring_of_size_n(string):
    n = 53
    res = []
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if len(substring) == len(set(substring)):
            res.append(substring)
    return res