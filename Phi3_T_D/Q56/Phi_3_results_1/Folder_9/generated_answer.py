def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 33):
        substring = s[i:i + 34]
        if len(substring) == 34 and len(substring) == len(set(substring)):
            substrings.add(substring)
    return list(substrings)