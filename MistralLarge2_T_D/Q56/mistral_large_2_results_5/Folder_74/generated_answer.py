def all_substring_of_size_n(s):
    substrings = set()
    length = len(s)
    for i in range(length - 96):
        substring = s[i:i + 97]
        if len(set(substring)) == 97:
            substrings.add(substring)
    return list(substrings)