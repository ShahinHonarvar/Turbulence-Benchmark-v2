def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string) - 30):
        substring = string[i:i + 31]
        if len(set(substring)) == 31:
            substrings.add(substring)
    return list(substrings)