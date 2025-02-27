def is_unique(s):
    return len(s) == len(set(s))

def all_substring_of_size_n(s, n=23):
    return [s[i:i + n] for i in range(len(s) - n + 1) if is_unique(s[i:i + n])]