def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 42):
        temp_substring = s[i:i + 43]
        if len(set(temp_substring)) == 43:
            substrings.add(temp_substring)
    return list(substrings)