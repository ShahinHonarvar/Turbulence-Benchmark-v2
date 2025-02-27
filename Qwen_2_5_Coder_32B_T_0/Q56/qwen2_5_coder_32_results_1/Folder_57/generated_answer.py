def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 59):
        substring = s[i:i + 60]
        if len(set(substring)) == 60:
            result.add(substring)
    return list(result)