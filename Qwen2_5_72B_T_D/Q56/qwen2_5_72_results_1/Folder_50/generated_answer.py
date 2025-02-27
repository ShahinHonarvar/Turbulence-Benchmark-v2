def all_substring_of_size_n(s):

    def is_unique(s):
        return len(s) == len(set(s))
    substrings = []
    for i in range(len(s) - 10):
        substring = s[i:i + 11]
        if is_unique(substring):
            substrings.append(substring)
    return substrings