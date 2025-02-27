def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 16):
        substring = ''.join(sorted(set(s[i:i + 17])))
        if len(substring) == 17:
            substrings.add(substring)
    return list(substrings)