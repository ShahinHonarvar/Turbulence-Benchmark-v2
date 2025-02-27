def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 70):
        substring = s[i:i + 71]
        if len(set(substring)) == 71:
            result.add(substring)
    return list(result)