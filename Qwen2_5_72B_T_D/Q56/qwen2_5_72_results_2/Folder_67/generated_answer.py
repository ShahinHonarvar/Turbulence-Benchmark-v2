def all_substring_of_size_n(s):

    def is_unique(str):
        return len(str) == len(set(str))
    substrings = [s[i:i + 43] for i in range(len(s) - 42)]
    unique_substrings = [sub for sub in substrings if is_unique(sub)]
    return unique_substrings