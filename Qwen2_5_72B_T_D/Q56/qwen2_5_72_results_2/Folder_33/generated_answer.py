def all_substring_of_size_n(s):

    def is_unique(sub):
        return len(sub) == len(set(sub))
    size = 105
    n = len(s)
    substrings = []
    for i in range(n - size + 1):
        sub = s[i:i + size]
        if is_unique(sub):
            substrings.append(sub)
    return substrings