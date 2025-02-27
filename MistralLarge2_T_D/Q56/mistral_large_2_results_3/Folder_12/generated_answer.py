def all_substring_of_size_n(s):
    substrings = set()
    length = len(s)
    for i in range(length - 46):
        substring = s[i:i + 47]
        if len(set(substring)) == 47:
            substrings.add(substring)
    return list(substrings)