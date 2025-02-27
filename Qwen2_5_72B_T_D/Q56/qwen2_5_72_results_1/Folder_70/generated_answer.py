def all_substring_of_size_n(s):

    def is_distinct(sub):
        return len(sub) == len(set(sub))
    n = 12
    return [s[i:i + n] for i in range(len(s) - n + 1) if is_distinct(s[i:i + n])]