def all_substring_of_size_n(s):

    def is_distinct_chars(sub):
        return len(set(sub)) == len(sub)
    n = 110
    substrings = []
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if is_distinct_chars(sub):
            substrings.append(sub)
    return substrings