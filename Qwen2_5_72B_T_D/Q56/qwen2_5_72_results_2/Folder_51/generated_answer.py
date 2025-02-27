def all_substring_of_size_n(s):

    def is_unique_chars(sub):
        return len(sub) == len(set(sub))
    n = len(s)
    if n < 96:
        return []
    result = []
    for i in range(n - 95):
        sub = s[i:i + 96]
        if is_unique_chars(sub):
            result.append(sub)
    return result