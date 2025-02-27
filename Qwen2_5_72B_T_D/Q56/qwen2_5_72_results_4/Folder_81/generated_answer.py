def all_substring_of_size_n(s):

    def is_unique_chars(st):
        return len(st) == len(set(st))
    n = 98
    substrings = []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if is_unique_chars(substring):
            substrings.append(substring)
    return substrings