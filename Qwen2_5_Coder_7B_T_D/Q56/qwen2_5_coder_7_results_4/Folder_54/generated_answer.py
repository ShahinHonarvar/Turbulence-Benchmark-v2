def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 27):
        substring = s[i:i + 28]
        if len(substring) == len(set(substring)):
            substrings.add(substring)
    return list(substrings)