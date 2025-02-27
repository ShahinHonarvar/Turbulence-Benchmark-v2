def all_substring_of_size_n(s):
    result_set = set()
    for i in range(len(s) - 28):
        if len(set(s[i:i + 29])) == 29:
            result_set.add(s[i:i + 29])
    return list(result_set)