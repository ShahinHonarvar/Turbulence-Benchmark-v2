def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 20):
        substring = s[i:i + 21]
        if len(set(substring)) == 21:
            result.add(substring)
    return list(result)