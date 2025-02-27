def all_substring_of_size_n(s):
    result = []
    window_size = 25
    for i in range(len(s) - window_size + 1):
        window = s[i:i + window_size]
        if len(set(window)) == window_size:
            result.append(window)
    return result