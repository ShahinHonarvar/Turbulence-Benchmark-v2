def all_substring_of_size_n(s):

    def is_unique(sub):
        return len(sub) == len(set(sub))
    n = 92
    substrings = []
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if is_unique(sub):
            substrings.append(sub)
    return substrings