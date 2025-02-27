def all_substring_of_size_n(s):

    def is_unique(sub):
        return len(set(sub)) == len(sub)
    n = 32
    substrings = [s[i:i + n] for i in range(len(s) - n + 1)]
    unique_substrings = list(filter(is_unique, substrings))
    return unique_substrings