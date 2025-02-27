def all_substring_of_size_n(s):
    n = 52
    result = []
    length = len(s)
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            result.append(substring)
    return list(set(result))