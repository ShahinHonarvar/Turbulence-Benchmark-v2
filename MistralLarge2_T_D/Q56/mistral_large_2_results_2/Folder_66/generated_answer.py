def all_substring_of_size_n(s):
    return [s[i:i + 26] for i in range(len(s) - 25) if len(set(s[i:i + 26])) == 26]