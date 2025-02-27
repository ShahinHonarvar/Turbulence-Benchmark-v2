def all_substring_of_size_n(s):

    def valid_substring(substring):
        return len(set(substring)) == 40
    substrings_set = set()
    n = 40
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if valid_substring(substring):
            substrings_set.add(substring)
    return list(substrings_set)