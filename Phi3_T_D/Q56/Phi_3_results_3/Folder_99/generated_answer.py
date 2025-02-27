def all_substring_of_size_n(string):
    substrings_set = set()
    length = 110
    for i in range(len(string) - length + 1):
        substring = string[i:i + length]
        if len(set(substring)) == length:
            substrings_set.add(substring)
    return list(substrings_set)