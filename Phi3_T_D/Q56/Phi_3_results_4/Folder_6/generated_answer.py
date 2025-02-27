def all_substring_of_size_n(s):
    unique_substrings = set()
    for i in range(len(s) - 22):
        substring = s[i:i + 23]
        if len(set(substring)) == 23:
            unique_substrings.add(substring)
    return list(unique_substrings)