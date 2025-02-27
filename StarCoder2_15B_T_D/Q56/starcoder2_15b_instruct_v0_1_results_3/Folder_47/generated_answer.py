def all_substring_of_size_n(s):
    result = []
    n = 91
    for i in range(len(s) - n + 1):
        window = s[i:i + n]
        if len(window) == len(set(window)):
            result.append(window)
    return result