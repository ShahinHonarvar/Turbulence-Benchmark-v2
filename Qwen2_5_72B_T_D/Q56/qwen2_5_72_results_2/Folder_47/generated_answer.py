def all_substring_of_size_n(s):

    def is_unique(sub):
        return len(set(sub)) == len(sub)
    n = 91
    substrings = [s[i:i + n] for i in range(len(s) - n + 1)]
    unique_substrings = [sub for sub in substrings if is_unique(sub)]
    return unique_substrings