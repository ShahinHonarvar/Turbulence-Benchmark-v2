def all_substring_of_size_n(s):
    N = 28
    unique_substrings = set()
    for i in range(len(s) - N + 1):
        substring = s[i:i + N]
        if len(substring) == len(set(substring)):
            unique_substrings.add(substring)
    return list(unique_substrings)