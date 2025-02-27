def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 57 + 1):
        substring = s[i:i + 57]
        if len(set(substring)) == 57:
            result.add(substring)
    return list(result)