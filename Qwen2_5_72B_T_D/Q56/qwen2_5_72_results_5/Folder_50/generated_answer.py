def all_substring_of_size_n(s):

    def is_distinct(sub):
        return len(sub) == len(set(sub))
    n = 11
    substrings = [s[i:i + n] for i in range(len(s) - n + 1)]
    distinct_substrings = [sub for sub in substrings if is_distinct(sub)]
    return distinct_substrings