def all_substring_of_size_n(s):

    def is_unique(sub):
        return len(sub) == len(set(sub))
    length = 9
    n = len(s)
    substrings = []
    for i in range(n - length + 1):
        sub = s[i:i + length]
        if is_unique(sub):
            substrings.append(sub)
    return substrings