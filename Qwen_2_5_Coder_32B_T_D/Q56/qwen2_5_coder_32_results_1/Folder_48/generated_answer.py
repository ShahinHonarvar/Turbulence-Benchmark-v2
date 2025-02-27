def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 119):
        if len(set(s[i:i + 120])) == 120:
            substrings.add(s[i:i + 120])
    return list(substrings)