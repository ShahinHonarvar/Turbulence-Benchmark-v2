def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string) - 38 + 1):
        substring = string[i:i + 38]
        if len(set(substring)) == 38:
            substrings.add(substring)
    return list(substrings)