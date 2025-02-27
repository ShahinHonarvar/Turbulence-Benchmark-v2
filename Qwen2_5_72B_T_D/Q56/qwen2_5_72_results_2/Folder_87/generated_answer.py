def all_substring_of_size_n(s):

    def is_unique_chars(sub):
        return len(sub) == len(set(sub))
    n = 58
    substrings = [s[i:i + n] for i in range(len(s) - n + 1)]
    result = [sub for sub in substrings if is_unique_chars(sub)]
    return result