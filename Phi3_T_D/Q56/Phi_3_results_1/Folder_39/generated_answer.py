def all_substring_of_size_n(s):
    result = set()
    length_n = 94
    for i in range(len(s) - length_n + 1):
        substring = s[i:i + length_n]
        if len(set(substring)) == length_n:
            result.add(substring)
    return list(result)