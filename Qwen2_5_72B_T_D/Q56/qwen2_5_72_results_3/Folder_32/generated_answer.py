def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 70):
        substring = s[i:i + 71]
        if len(set(substring)) == 71:
            substrings.append(substring)
    return list(set(substrings))