def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 43):
        substring = s[i:i + 44]
        if len(set(substring)) == 44:
            substrings.append(substring)
    return substrings