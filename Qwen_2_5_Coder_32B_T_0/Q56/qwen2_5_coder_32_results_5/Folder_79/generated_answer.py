def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 60):
        substring = s[i:i + 61]
        if len(set(substring)) == 61:
            result.add(substring)
    return list(result)