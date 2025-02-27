def all_substring_of_size_n(s):

    def is_valid_substring(substring):
        return len(substring) == 40 and len(set(substring)) == 40
    substrings = []
    for i in range(len(s) - 39):
        substring = s[i:i + 40]
        if is_valid_substring(substring):
            substrings.append(substring)
    return substrings