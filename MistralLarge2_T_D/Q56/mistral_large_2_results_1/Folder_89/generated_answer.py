def all_substring_of_size_n(s):
    substrings = set()
    length = len(s)
    for i in range(length - 37):
        substring = s[i:i + 38]
        if len(set(substring)) == 38:
            substrings.add(substring)
    return list(substrings)