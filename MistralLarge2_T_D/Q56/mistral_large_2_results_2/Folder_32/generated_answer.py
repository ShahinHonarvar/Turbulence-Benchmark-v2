def all_substring_of_size_n(s):
    substrings = set()
    length = len(s)
    for i in range(length - 70):
        substring = s[i:i + 71]
        if len(set(substring)) == 71:
            substrings.add(substring)
    return list(substrings)