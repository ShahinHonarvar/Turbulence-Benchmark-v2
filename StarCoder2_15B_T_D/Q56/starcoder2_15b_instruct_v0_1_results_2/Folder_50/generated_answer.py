def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 10):
        substring = s[i:i + 11]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings