def all_substring_of_size_n(string):
    n = 75
    result = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if len(substring) == len(set(substring)):
            result.add(substring)
    return list(result)