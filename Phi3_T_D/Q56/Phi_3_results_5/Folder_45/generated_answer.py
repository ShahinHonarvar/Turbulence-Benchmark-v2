def all_substring_of_size_n(s):
    distinct_substrings = set()
    for i in range(len(s) - 28):
        substring = s[i:i + 29]
        if len(set(substring)) == 29:
            distinct_substrings.add(substring)
    return list(distinct_substrings)