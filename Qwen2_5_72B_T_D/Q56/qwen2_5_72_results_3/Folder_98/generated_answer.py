def all_substring_of_size_n(s):

    def is_unique(sub):
        return len(sub) == len(set(sub))
    n = 10
    substrings = [s[i:i + n] for i in range(len(s) - n + 1) if is_unique(s[i:i + n])]
    return list(set(substrings))