def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 123):
        substring = s[i:i + 124]
        if len(substring) == 124 and len(substring) == len(set(substring)):
            result.add(substring)
    return list(result)