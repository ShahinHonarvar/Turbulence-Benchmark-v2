def all_substring_of_size_n(s):
    length = 12
    substrings_set = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if len(set(substring)) == length:
            substrings_set.add(substring)
    return list(substrings_set)