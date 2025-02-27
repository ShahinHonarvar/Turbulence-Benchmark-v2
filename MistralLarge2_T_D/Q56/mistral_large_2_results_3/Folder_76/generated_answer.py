def all_substring_of_size_n(s):
    substrings = set()
    length = len(s)
    for i in range(length - 148):
        substr = s[i:i + 149]
        if len(set(substr)) == 149:
            substrings.add(substr)
    return list(substrings)