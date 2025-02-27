def all_substring_of_size_n(string):
    result = []
    for i in range(len(string) - 2):
        substring = string[i:i + 3]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return result