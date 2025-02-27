def all_substring_of_size_n(string):
    distinct_substrings = set()
    n = 29
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if len(set(substring)) == n:
            distinct_substrings.add(substring)
    return list(distinct_substrings)