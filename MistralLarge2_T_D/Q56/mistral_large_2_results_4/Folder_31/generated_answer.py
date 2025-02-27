def all_substring_of_size_n(s):
    substrings = set()
    length = len(s)
    for i in range(length - 45):
        substring = s[i:i + 46]
        if len(set(substring)) == 46:
            substrings.add(substring)
    return list(substrings)