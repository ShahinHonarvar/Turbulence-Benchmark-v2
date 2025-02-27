def all_substring_of_size_n(s):

    def is_unique_chars(st):
        return len(st) == len(set(st))
    length = 63
    substrings = []
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if is_unique_chars(substring):
            substrings.append(substring)
    return substrings