def all_substring_of_size_n(s):
    distinct_substrings = set()
    for i in range(len(s) - 93):
        substring = s[i:i + 94]
        if len(set(substring)) == 94:
            distinct_substrings.add(substring)
    return list(distinct_substrings)