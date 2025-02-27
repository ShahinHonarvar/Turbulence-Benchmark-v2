def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 15):
        candidate = s[i:i + 16]
        if len(set(candidate)) == 16:
            substrings.add(candidate)
    return list(substrings)