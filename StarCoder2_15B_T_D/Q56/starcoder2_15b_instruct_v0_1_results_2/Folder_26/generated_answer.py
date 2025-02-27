def all_substring_of_size_n(string):
    distinct_substrings = set()
    for start in range(len(string) - substring_length + 1):
        for end in range(start + substring_length, len(string) + 1):
            substring = string[start:end]
            if len(set(substring)) == substring_length:
                distinct_substrings.add(substring)
    return list(distinct_substrings)