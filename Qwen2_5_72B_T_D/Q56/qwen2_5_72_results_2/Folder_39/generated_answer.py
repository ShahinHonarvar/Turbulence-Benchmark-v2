def all_substring_of_size_n(s):

    def is_unique_chars(st):
        return len(set(st)) == len(st)
    length = 94
    substrings = []
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if is_unique_chars(substring):
            substrings.append(substring)
    return substrings