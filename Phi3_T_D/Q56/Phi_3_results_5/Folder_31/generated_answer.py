def all_substring_of_size_n(s):
    distinct_substrings = {s[i:i + 46] for i in range(len(s) - 45) if len(set(s[i:i + 46])) == 46}
    return list(distinct_substrings)