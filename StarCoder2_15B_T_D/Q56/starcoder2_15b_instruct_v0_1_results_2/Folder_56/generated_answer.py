def all_substring_of_size_n(string):
    substrings = []
    if len(string) >= 69:
        for i in range(len(string) - 69 + 1):
            substring = string[i:i + 69]
            if len(substring) == len(set(substring)):
                substrings.append(substring)
    return substrings