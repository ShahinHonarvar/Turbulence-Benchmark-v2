def all_substring_of_size_n(s):
    unique_substrings = set()
    if len(s) < 88:
        return list(unique_substrings)
    for i in range(len(s) - 87):
        substring = s[i:i + 88]
        if len(set(substring)) == 88:
            unique_substrings.add(substring)
    return list(unique_substrings)