def all_substring_of_size_n(s):
    result = []
    n = 32
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            result.append(substring)
    return result