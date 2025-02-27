def all_substring_of_size_n(s):
    n = 146
    unique_substrings = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            unique_substrings.add(substring)
    return list(unique_substrings)