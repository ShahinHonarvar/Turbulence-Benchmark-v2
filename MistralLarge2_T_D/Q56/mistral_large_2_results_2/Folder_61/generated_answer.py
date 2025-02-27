def all_substring_of_size_n(s):
    substrings = set()
    length = len(s)
    for i in range(length - 38):
        substring = s[i:i + 39]
        if len(set(substring)) == 39:
            substrings.add(substring)
    return list(substrings)