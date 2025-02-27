def all_substring_of_size_n(s):
    return [s[i:i + 96] for i in range(len(s) - 95) if len(set(s[i:i + 96])) == 96]