def all_substring_of_size_n(s):
    if len(s) <= 46:
        return []
    substrings = set()
    for i in range(len(s) - 45):
        substring = s[i:i + 46]
        if len(set(substring)) == 46:
            substrings.add(substring)
    return list(substrings)