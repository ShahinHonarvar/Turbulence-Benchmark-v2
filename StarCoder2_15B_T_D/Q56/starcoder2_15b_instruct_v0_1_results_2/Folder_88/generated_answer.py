def all_substring_of_size_n(s: str) -> list:
    n = 68
    result = []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return result