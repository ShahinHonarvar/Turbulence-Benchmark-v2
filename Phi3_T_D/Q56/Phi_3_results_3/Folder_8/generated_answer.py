def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 29):
        sub = s[i:i + 30]
        if len(set(sub)) == 30:
            substrings.add(sub)
    return list(substrings)