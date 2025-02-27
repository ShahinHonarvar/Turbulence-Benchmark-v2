def all_substring_of_size_n(string):
    n = 43
    return [string[i:i + n] for i in range(len(string) - n + 1) if len(set(string[i:i + n])) == n]