def all_substring_of_size_n(string):
    result = []
    for start in range(len(string) - 120 + 1):
        for end in range(start + 120, len(string) + 1):
            substring = string[start:end]
            if len(substring) == len(set(substring)):
                result.append(substring)
    return result