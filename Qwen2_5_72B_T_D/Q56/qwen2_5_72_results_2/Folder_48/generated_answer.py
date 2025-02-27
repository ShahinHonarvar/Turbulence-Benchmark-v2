def all_substring_of_size_n(s):

    def is_unique_chars(sub):
        return len(sub) == len(set(sub))
    result = []
    for i in range(len(s) - 119):
        substring = s[i:i + 120]
        if is_unique_chars(substring):
            result.append(substring)
    return result