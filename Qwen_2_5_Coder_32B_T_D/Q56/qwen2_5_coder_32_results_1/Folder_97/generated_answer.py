def all_substring_of_size_n(s):
    unique_substrings = set()
    for i in range(len(s) - 142 + 1):
        substring = s[i:i + 142]
        if len(set(substring)) == 142:
            unique_substrings.add(substring)
    return list(unique_substrings)