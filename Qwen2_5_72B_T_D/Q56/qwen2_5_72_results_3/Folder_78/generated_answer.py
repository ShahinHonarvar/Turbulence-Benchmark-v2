def all_substring_of_size_n(s):

    def is_unique(s):
        return len(s) == len(set(s))
    result = []
    for i in range(len(s) - 48):
        substring = s[i:i + 49]
        if is_unique(substring):
            result.append(substring)
    return result