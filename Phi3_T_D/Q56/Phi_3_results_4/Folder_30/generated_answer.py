def all_substring_of_size_n(s):
    length = 79
    distinct_substrings = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if len(set(substring)) == length:
            distinct_substrings.add(substring)
    return list(distinct_substrings)