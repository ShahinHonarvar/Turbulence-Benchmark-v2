def all_substring_of_size_n(s):
    unique_substrings = set()
    for i in range(len(s) - 76):
        substring = ''.join(sorted(s[i:i + 77]))
        if len(set(substring)) == 77:
            unique_substrings.add(substring)
    return list(unique_substrings)