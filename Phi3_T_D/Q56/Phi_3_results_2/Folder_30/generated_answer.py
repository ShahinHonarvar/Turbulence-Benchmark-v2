def all_substring_of_size_n(s):
    n = 79
    unique_substrings = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == 79:
            unique_substrings.add(substring)
    return list(unique_substrings)