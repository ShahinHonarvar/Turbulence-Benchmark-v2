def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 78):
        substr = s[i:i + 79]
        if len(set(substr)) == 79:
            substrings.add(substr)
    return list(substrings)