def all_substring_of_size_n(s):

    def is_unique_chars(sub):
        return len(set(sub)) == len(sub)
    n = 16
    if n > len(s):
        return []
    substrings = []
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if is_unique_chars(sub):
            substrings.append(sub)
    return substrings