def all_substring_of_size_n(str):
    distinct_substrings = []
    n = 85
    if len(str) < n:
        return []
    for i in range(len(str) - n + 1):
        substring = str[i:i + n]
        if len(substring) == len(set(substring)):
            distinct_substrings.append(substring)
    return distinct_substrings