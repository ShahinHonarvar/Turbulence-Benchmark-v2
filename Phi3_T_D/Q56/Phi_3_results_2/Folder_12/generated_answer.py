def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 46):
        substring = s[i:i + 47]
        if len(set(substring)) == 47:
            if substring not in substrings:
                substrings.append(substring)
    return substrings