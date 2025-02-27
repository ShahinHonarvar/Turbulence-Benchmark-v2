def all_substring_of_size_n(s):

    def is_unique(string):
        return len(string) == len(set(string))
    result = []
    n = 85
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if is_unique(substring):
            result.append(substring)
    return result