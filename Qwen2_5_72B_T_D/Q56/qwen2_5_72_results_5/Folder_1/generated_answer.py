def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 24:
        return substrings
    for i in range(len(s) - 23):
        substring = s[i:i + 24]
        if len(set(substring)) == 24:
            substrings.append(substring)
    return substrings