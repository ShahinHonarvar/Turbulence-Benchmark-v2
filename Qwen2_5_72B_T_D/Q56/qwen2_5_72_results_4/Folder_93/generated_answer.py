def all_substring_of_size_n(s):

    def is_unique_chars(sub):
        return len(sub) == len(set(sub))
    result = []
    n = 54
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if is_unique_chars(sub):
            result.append(sub)
    return result