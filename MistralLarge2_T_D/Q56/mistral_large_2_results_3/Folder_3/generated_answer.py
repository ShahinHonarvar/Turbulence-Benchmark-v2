def all_substring_of_size_n(s):
    substrings = set()
    length = len(s)
    for i in range(length - 92):
        substring = s[i:i + 93]
        if len(set(substring)) == 93:
            substrings.add(substring)
    return list(substrings)