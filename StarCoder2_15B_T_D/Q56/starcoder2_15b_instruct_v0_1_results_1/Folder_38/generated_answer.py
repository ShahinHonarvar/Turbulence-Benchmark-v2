def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string) - 34):
        substring = string[i:i + 35]
        if len(set(substring)) == 35:
            substrings.add(substring)
    return list(substrings)