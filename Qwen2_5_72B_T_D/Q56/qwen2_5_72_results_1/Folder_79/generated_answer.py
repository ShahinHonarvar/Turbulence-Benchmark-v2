def all_substring_of_size_n(s):

    def is_unique_chars(sub):
        return len(set(sub)) == len(sub)
    n = len(s)
    if n < 61:
        return []
    substrings = []
    for i in range(n - 60):
        sub = s[i:i + 61]
        if is_unique_chars(sub):
            substrings.append(sub)
    return substrings