def all_substring_of_size_n(s):

    def is_distinct_chars(sub):
        return len(sub) == len(set(sub))
    substrings = []
    for i in range(len(s) - 19):
        substring = s[i:i + 20]
        if is_distinct_chars(substring):
            substrings.append(substring)
    return substrings