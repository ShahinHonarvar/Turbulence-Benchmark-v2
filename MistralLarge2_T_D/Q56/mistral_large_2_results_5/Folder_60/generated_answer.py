def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 35):
        substr = s[i:i + 36]
        if len(set(substr)) == 36:
            substrings.add(substr)
    return list(substrings)