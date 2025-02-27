def all_substrings_of_size_n(string):
    n = 64
    result = []
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return result