def all_substring_of_size_n(s):
    length = 95
    return list({s[i:i + length] for i in range(len(s) - length + 1) if len(set(s[i:i + length])) == length})