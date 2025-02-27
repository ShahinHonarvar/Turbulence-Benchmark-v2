def all_substring_of_size_n(s):

    def is_unique(sub):
        return len(set(sub)) == len(sub)
    substrings = [s[i:i + 70] for i in range(len(s) - 69)]
    unique_substrings = [sub for sub in substrings if is_unique(sub)]
    return unique_substrings