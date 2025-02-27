def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 113):
        substring = s[i:i + 114]
        if len(set(substring)) == 114:
            result.add(substring)
    return list(result)