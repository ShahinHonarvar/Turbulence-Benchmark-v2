def all_substring_of_size_n(s):

    def is_distinct(sub):
        return len(sub) == len(set(sub))
    result = []
    for i in range(len(s) - 109):
        sub = s[i:i + 110]
        if is_distinct(sub):
            result.append(sub)
    return result