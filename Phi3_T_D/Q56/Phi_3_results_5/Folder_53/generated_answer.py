def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 24):
        candidate = s[i:i + 25]
        if len(set(candidate)) == 25:
            substrings.add(candidate)
    return list(substrings)