def all_substring_of_size_n(s):

    def is_distinct(sub):
        return len(sub) == len(set(sub))
    result = []
    for i in range(len(s) - 62):
        substring = s[i:i + 63]
        if is_distinct(substring):
            result.append(substring)
    return result