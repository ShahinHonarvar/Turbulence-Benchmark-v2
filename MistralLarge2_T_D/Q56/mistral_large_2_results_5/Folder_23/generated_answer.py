def all_substring_of_size_n(s):

    def has_unique_chars(substring):
        return len(set(substring)) == len(substring)
    substrings = set()
    for i in range(len(s) - 41):
        substring = s[i:i + 42]
        if has_unique_chars(substring):
            substrings.add(substring)
    return list(substrings)