def all_substring_of_size_n(s):

    def is_unique(sub):
        return len(sub) == len(set(sub))
    n = 9
    result = []
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if is_unique(sub):
            result.append(sub)
    return result