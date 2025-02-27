def all_substring_of_size_n(s):

    def has_no_duplicate_chars(sub):
        return len(sub) == len(set(sub))
    n = 17
    substrings = [s[i:i + n] for i in range(len(s) - n + 1)]
    valid_substrings = [sub for sub in substrings if has_no_duplicate_chars(sub)]
    return valid_substrings