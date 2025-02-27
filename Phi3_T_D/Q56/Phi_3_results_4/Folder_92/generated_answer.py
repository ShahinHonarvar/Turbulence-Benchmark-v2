def all_substring_of_size_n(s):
    substrings = {s[i:i + 9] for i in range(len(s) - 8)}
    unique_substrings = [sub for sub in substrings if len(set(sub)) == 9]
    return unique_substrings