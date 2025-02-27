def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 59):
        substr = s[i:i + 60]
        if len(substr) == 60 and len(set(substr)) == 60:
            substrings.add(substr)
    return list(substrings)