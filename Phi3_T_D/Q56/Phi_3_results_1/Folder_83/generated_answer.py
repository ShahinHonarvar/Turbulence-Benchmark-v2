def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 47):
        substr = s[i:i + 48]
        if len(set(substr)) == 48:
            substrings.add(substr)
    return list(substrings)