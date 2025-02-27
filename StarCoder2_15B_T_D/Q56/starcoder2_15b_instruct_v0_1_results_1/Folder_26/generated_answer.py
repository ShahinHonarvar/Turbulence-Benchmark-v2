def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string) - 2):
        substring = string[i:i + 3]
        if len(set(substring)) == 3:
            substrings.add(substring)
    return list(substrings)