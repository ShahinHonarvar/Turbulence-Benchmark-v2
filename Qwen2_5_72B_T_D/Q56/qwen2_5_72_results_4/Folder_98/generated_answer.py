def all_substring_of_size_n(s):

    def is_unique(sub):
        return len(set(sub)) == len(sub)
    substrings = []
    n = 10
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if is_unique(sub):
            substrings.append(sub)
    return substrings