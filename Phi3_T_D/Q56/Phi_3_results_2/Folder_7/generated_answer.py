def all_substring_of_size_n(s):
    length = 117
    if len(s) < length:
        return []
    substrings = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if len(substring) == len(set(substring)):
            substrings.add(substring)
    return list(substrings)