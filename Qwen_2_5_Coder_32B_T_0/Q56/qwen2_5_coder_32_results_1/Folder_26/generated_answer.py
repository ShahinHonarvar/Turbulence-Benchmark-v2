def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 32):
        substring = s[i:i + 33]
        if len(set(substring)) == 33:
            result.add(substring)
    return list(result)