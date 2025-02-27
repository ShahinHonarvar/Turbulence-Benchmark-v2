def all_substring_of_size_n(s):
    n = 52
    result_set = set()
    for i in range(len(s) - n + 1):
        current_substring = s[i:i + n]
        if len(set(current_substring)) == n:
            result_set.add(current_substring)
    return list(result_set)