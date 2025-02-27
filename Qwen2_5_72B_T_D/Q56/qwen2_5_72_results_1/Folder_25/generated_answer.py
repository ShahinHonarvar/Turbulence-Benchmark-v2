def all_substring_of_size_n(s):
    substring_length = 67
    substrings = set()
    for i in range(len(s) - substring_length + 1):
        substring = s[i:i + substring_length]
        if len(set(substring)) == substring_length:
            substrings.add(substring)
    return list(substrings)