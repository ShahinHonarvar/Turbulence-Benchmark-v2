def all_substring_of_size_n(s):
    unique_substrings = set()
    for i in range(len(s) - 10):
        substring = s[i:i + 11]
        if len(set(substring)) == 11:
            unique_substrings.add(substring)
    return list(unique_substrings)