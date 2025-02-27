def all_substring_of_size_n(string):
    distinct_substrings = set()
    for i in range(len(string) - 31):
        substring = string[i:i + 32]
        if len(set(substring)) == 32:
            distinct_substrings.add(substring)
    return list(distinct_substrings)