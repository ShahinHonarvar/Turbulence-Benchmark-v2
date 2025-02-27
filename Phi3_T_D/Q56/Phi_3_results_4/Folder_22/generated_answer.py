def all_substring_of_size_n(s):
    distinct_substrings = set()
    for i in range(len(s) - 21):
        substring = s[i:i + 22]
        if len(set(substring)) == 22:
            distinct_substrings.add(substring)
    return list(distinct_substrings)