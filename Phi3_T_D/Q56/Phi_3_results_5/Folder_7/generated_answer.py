def all_substring_of_size_n(s):
    all_substrings = set([s[i:i + 117] for i in range(len(s) - 116)])
    distinct_substrings = [sub for sub in all_substrings if len(set(sub)) == 117]
    return distinct_substrings