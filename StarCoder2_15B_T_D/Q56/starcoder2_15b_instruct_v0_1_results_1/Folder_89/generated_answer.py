def all_substring_of_size_n(string):
    n = 38
    if len(string) < n:
        return []
    substrings = set((string[i:i + n] for i in range(len(string) - n + 1)))
    if len(substrings) < n:
        return []
    return list(substrings)