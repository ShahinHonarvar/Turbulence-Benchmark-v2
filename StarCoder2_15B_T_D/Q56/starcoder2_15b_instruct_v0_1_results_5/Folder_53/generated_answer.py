def all_substring_of_size_n(string):
    if len(string) < 25:
        return []
    unique_substrings = set()
    for i in range(len(string) - 24):
        substring = string[i:i + 25]
        if len(substring) == len(set(substring)):
            unique_substrings.add(substring)
    return list(unique_substrings)