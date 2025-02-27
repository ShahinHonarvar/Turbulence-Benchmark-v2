def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 68):
        sub = s[i:i + 69]
        if len(set(sub)) == 69:
            substrings.add(sub)
    return list(substrings)