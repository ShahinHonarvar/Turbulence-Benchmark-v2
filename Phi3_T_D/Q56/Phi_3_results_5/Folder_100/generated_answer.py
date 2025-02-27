def all_substring_of_size_n(s):
    distinct_substrings = set()
    for i in range(len(s) - 91):
        substring = s[i:i + 92]
        if len(set(substring)) == 92:
            distinct_substrings.add(substring)
    return list(distinct_substrings)