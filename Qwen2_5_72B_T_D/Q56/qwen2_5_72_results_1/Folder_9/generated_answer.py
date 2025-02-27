def all_substring_of_size_n(s):

    def is_unique_chars(sub):
        return len(set(sub)) == len(sub)
    n = 34
    substrings = [s[i:i + n] for i in range(len(s) - n + 1) if is_unique_chars(s[i:i + n])]
    return substrings