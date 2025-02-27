def all_substring_of_size_n(s):
    length = len(s)
    if length < 149:
        return []
    substrings = set()
    for i in range(length - 148):
        substring = s[i:i + 149]
        if len(set(substring)) == 149:
            substrings.add(substring)
    return list(substrings)