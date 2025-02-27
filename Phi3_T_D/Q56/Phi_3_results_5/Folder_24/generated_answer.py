def all_substring_of_size_n(s):
    unique_substrings = set()
    for i in range(len(s) - 51):
        substring = s[i:i + 52]
        if len(set(substring)) == 52:
            unique_substrings.add(substring)
    return list(unique_substrings)