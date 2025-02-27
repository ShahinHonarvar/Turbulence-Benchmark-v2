def all_substring_of_size_n(s):

    def is_unique(s):
        return len(s) == len(set(s))
    substrings = set()
    n = 17
    if len(s) < n:
        return []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if is_unique(substring):
            substrings.add(substring)
    return list(substrings)