def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 48):
        substring = s[i:i + 49]
        if len(substring) == 49 and len(substring) == len(set(substring)):
            result.add(substring)
    return list(result)