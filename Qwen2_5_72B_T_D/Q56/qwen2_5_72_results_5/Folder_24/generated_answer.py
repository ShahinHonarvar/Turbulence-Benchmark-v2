def all_substring_of_size_n(s):

    def is_unique_chars(sub):
        return len(set(sub)) == len(sub)
    n = 52
    result = []
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if is_unique_chars(sub):
            result.append(sub)
    return result