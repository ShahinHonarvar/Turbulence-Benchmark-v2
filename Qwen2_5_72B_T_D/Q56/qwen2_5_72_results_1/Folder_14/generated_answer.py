def all_substring_of_size_n(s):

    def is_unique(s):
        return len(s) == len(set(s))
    substrings = []
    n = 85
    if n > len(s):
        return substrings
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if is_unique(substring):
            substrings.append(substring)
    return substrings