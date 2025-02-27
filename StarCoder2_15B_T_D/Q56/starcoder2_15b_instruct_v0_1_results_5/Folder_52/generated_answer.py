def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string) - 14):
        substring = string[i:i + 15]
        if len(set(substring)) == 15:
            substrings.add(substring)
    return list(substrings)