def all_substring_of_size_n(s):

    def is_unique(s):
        return len(s) == len(set(s))
    length = 99
    substrings = [s[i:i + length] for i in range(len(s) - length + 1)]
    unique_substrings = [sub for sub in substrings if is_unique(sub)]
    return unique_substrings