def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 37):
        substring = s[i:i + 38]
        if len(set(substring)) == 38:
            result.add(substring)
    return list(result)