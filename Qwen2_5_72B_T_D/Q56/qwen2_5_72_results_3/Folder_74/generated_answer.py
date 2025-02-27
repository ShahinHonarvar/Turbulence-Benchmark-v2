def all_substring_of_size_n(s):

    def is_distinct_chars(sub):
        return len(sub) == len(set(sub))
    length = len(s)
    n = 97
    substrings = []
    if length < n:
        return substrings
    for i in range(length - n + 1):
        sub = s[i:i + n]
        if is_distinct_chars(sub):
            substrings.append(sub)
    return substrings