def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 117 + 1):
        substring = s[i:i + 117]
        if len(set(substring)) == 117:
            substrings.append(substring)
    return substrings