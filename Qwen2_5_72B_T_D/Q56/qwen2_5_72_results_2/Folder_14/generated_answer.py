def all_substring_of_size_n(s):

    def is_unique(s):
        return len(s) == len(set(s))
    length = 85
    result = []
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if is_unique(substring):
            result.append(substring)
    return result