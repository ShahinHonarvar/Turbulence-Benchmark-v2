def all_substring_of_size_n(s):
    length = 78
    substrings = set()
    for i in range(len(s) - length + 1):
        substr = s[i:i + length]
        if len(set(substr)) == length:
            substrings.add(substr)
    return list(substrings)