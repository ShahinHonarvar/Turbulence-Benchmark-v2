def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 143 + 1):
        substring = string[i:i + 143]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings