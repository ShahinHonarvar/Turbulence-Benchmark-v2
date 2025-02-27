def all_substring_of_size_n(s):
    if len(s) < 44:
        return []
    substrings = set()
    for i in range(len(s) - 43):
        substring = s[i:i + 44]
        if len(set(substring)) == 44:
            substrings.add(substring)
    return list(substrings)