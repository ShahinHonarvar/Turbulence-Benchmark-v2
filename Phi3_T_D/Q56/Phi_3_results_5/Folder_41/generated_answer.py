def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 73):
        if len(set(s[i:i + 74])) == 74:
            substrings.add(s[i:i + 74])
    return list(substrings)