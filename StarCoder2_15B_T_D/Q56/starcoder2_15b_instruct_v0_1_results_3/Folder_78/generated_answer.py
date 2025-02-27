def all_substring_of_size_n(s):
    substrings = [s[i:i + 49] for i in range(len(s) - 48)]
    distinct_substrings = [substring for substring in substrings if len(set(substring)) == 49]
    return list(distinct_substrings)