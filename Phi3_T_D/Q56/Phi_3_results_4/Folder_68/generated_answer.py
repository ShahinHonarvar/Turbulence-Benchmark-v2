def all_substring_of_size_n(s):
    length = 75
    if len(s) < length:
        return []
    found_substrings = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if len(set(substring)) == length:
            found_substrings.add(substring)
    return list(found_substrings)