def all_substring_of_size_n(s):
    substrings = set()
    length = 130
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if len(set(substring)) == length:
            substrings.add(substring)
    return list(substrings)