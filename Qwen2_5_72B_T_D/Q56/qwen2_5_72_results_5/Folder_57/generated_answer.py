def all_substring_of_size_n(s):

    def is_unique_chars(sub):
        return len(sub) == len(set(sub))
    substrings = [s[i:i + 60] for i in range(len(s) - 59)]
    unique_substrings = [sub for sub in substrings if is_unique_chars(sub)]
    return unique_substrings