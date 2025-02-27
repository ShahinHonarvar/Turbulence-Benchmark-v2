def all_substring_of_size_n(s):

    def is_unique_chars(sub):
        return len(set(sub)) == len(sub)
    substrings = []
    n = len(s)
    for i in range(n - 5):
        sub = s[i:i + 6]
        if is_unique_chars(sub):
            substrings.append(sub)
    return substrings