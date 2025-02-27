def all_substring_of_size_n(s):

    def is_unique(str):
        return len(str) == len(set(str))
    substrings = []
    for i in range(len(s) - 48):
        substring = s[i:i + 49]
        if is_unique(substring):
            substrings.append(substring)
    return substrings