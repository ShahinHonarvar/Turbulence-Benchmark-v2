def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 19 + 1):
        substring = s[i:i + 19]
        if len(set(substring)) == 19:
            result.add(substring)
    return list(result)