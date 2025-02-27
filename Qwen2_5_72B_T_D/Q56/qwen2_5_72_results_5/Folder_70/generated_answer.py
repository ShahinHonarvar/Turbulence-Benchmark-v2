def all_substring_of_size_n(s):

    def is_unique_chars(sub):
        return len(sub) == len(set(sub))
    length = 12
    substrings = []
    for i in range(len(s) - length + 1):
        sub = s[i:i + length]
        if is_unique_chars(sub):
            substrings.append(sub)
    return substrings