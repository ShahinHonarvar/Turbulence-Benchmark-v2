def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 123):
        substring = s[i:i + 124]
        if len(set(substring)) == 124:
            result.add(substring)
    return list(result)