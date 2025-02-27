def all_substring_of_size_n(s):
    unique_substrings = set()
    for i in range(len(s) - 44):
        substring = s[i:i + 45]
        if len(set(substring)) == 45:
            unique_substrings.add(substring)
    return list(unique_substrings)