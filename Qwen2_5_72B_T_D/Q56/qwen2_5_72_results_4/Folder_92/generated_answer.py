def all_substring_of_size_n(s):

    def is_unique(subs):
        return len(subs) == len(set(subs))
    n = 9
    substrings = [s[i:i + n] for i in range(len(s) - n + 1) if is_unique(s[i:i + n])]
    return substrings