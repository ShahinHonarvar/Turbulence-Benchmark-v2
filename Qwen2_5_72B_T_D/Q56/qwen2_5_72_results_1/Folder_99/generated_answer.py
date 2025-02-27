def all_substring_of_size_n(s):

    def has_unique_chars(sub):
        return len(sub) == len(set(sub))
    substrings = []
    if len(s) < 110:
        return []
    for i in range(len(s) - 109):
        sub = s[i:i + 110]
        if has_unique_chars(sub):
            substrings.append(sub)
    return substrings