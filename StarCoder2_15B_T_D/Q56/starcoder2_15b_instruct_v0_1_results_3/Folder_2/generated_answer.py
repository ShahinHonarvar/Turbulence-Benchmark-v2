def all_substring_of_size_n(text):
    n = 56
    result = []
    for i in range(len(text) - n + 1):
        substring = text[i:i + n]
        if len(set(substring)) == n:
            result.append(substring)
    return result