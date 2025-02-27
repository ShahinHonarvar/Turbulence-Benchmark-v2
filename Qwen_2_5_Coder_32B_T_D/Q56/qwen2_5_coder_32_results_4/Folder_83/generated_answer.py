def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 47):
        substring = s[i:i + 48]
        if len(set(substring)) == 48:
            result.add(substring)
    return list(result)