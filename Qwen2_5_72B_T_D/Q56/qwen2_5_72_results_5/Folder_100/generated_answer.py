def all_substring_of_size_n(s):

    def is_unique_chars(sub):
        return len(sub) == len(set(sub))
    n = 92
    substrings = [s[i:i + n] for i in range(len(s) - n + 1)]
    unique_substrings = [sub for sub in substrings if is_unique_chars(sub)]
    return unique_substrings