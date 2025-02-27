def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 94):
        substring = s[i:i + 95]
        if len(substring) == len(set(substring)):
            result.add(substring)
    return list(result)