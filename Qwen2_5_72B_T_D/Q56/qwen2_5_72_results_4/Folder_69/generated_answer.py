def all_substring_of_size_n(s):

    def is_unique(sub):
        return len(sub) == len(set(sub))
    n = len(s)
    substrings = []
    for i in range(n - 98):
        sub = s[i:i + 99]
        if is_unique(sub):
            substrings.append(sub)
    return substrings