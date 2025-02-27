def all_substring_of_size_n(s):
    return [s[i:i + 91] for i in range(len(s) - 90) if len(set(s[i:i + 91])) == 91]