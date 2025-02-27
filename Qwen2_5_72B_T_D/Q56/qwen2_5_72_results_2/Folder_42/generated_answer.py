def all_substring_of_size_n(s):

    def is_unique(string):
        return len(string) == len(set(string))
    length = 45
    if len(s) < length:
        return []
    substrings = []
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if is_unique(substring):
            substrings.append(substring)
    return substrings