def all_substring_of_size_n(s):
    unique_substrings = set()
    for i in range(len(s) - 41):
        current_substring = s[i:i + 42]
        if len(set(current_substring)) == 42:
            unique_substrings.add(current_substring)
    return list(unique_substrings)