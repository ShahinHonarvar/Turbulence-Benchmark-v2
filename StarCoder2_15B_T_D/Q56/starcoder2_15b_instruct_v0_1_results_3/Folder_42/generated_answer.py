def all_substring_of_size_n(string):
    n = 45
    result = []
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if len(set(substring)) == n:
            result.append(substring)
    return result