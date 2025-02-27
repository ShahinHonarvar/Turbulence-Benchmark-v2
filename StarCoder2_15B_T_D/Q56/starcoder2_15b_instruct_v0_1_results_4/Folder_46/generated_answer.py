def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string) - 87 + 1):
        substring = string[i:i + 87]
        if len(substring) == len(set(substring)):
            substrings.add(substring)
    return list(substrings)