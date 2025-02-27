def all_substring_of_size_n(s):

    def has_no_duplicates(sub):
        return len(sub) == len(set(sub))
    result = []
    for i in range(len(s) - 49):
        substring = s[i:i + 50]
        if has_no_duplicates(substring):
            result.append(substring)
    return result