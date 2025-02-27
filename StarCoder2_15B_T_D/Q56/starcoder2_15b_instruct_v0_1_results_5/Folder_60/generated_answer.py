def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 36 + 1):
        substring = string[i:i + 36]
        if len(set(substring)) == 36:
            substrings.append(substring)
    return substrings