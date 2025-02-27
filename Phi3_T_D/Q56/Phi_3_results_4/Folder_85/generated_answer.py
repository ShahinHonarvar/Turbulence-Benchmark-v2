def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 13):
        if len(set(s[i:i + 14])) == 14:
            substrings.add(s[i:i + 14])
    return list(substrings)