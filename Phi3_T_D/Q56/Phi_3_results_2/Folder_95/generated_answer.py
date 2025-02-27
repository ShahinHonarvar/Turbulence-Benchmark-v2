def all_substring_of_size_n(s):
    length = 89
    substrings = set()
    for i in range(len(s) - length + 1):
        substring = ''.join(sorted(s[i:i + length]))
        if len(substring) == length:
            substrings.add(substring)
    return list(substrings)