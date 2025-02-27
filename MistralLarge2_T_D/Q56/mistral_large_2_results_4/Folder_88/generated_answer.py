def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 67):
        sub = s[i:i + 68]
        if len(set(sub)) == 68:
            substrings.add(sub)
    return list(substrings)