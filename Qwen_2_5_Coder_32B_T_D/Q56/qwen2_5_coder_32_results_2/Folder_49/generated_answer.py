def all_substring_of_size_n(s):
    substrings = set()
    l = len(s)
    for i in range(l - 72):
        sub = s[i:i + 73]
        if len(set(sub)) == 73:
            substrings.add(sub)
    return list(substrings)