def all_substring_of_size_n(s):
    substrings = {s[i:i + 60] for i in range(len(s) - 59)}
    unique_substrings = {sub for sub in substrings if len(set(sub)) == 60}
    return list(unique_substrings)