def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 62):
        substring = s[i:i + 63]
        if len(set(substring)) == 63:
            result.add(substring)
    return list(result)