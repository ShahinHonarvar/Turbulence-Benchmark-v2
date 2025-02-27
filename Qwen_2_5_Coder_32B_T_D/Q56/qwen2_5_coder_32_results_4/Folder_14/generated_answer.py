def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 84):
        substring = s[i:i + 85]
        if len(set(substring)) == 85:
            result.add(substring)
    return list(result)