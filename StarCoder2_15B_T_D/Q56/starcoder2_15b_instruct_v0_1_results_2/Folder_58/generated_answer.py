def all_substring_of_size_n(s):
    distinct_substrings = {}
    for i in range(len(s) - 127 + 1):
        substring = s[i:i + 127]
        if len(set(substring)) == 127:
            distinct_substrings[substring] = 1
    return list(distinct_substrings.keys())