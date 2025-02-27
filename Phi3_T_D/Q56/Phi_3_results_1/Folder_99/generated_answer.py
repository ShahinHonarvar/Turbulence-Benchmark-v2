def all_substring_of_size_n(s):
    length = 110
    unique_substrings = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if len(set(substring)) == length:
            unique_substrings.add(substring)
    return list(unique_substrings)