def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string) - 3):
        substring = string[i:i + 4]
        if len(set(substring)) == 4:
            substrings.add(substring)
    return list(substrings)