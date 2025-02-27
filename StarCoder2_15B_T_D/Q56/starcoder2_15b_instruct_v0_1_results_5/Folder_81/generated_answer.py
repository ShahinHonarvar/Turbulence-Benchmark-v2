def all_substring_of_size_n(text):
    result = []
    n = 98
    for i in range(len(text) - n + 1):
        substring = text[i:i + n]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return result