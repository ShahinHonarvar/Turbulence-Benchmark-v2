def all_substring_of_size_n(s):

    def is_unique_chars(sub):
        return len(sub) == len(set(sub))
    n = 146
    substrings = []
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if is_unique_chars(sub):
            substrings.append(sub)
    return substrings