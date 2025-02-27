def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 19):
        substring = s[i:i + 20]
        if len(set(substring)) == 20:
            result.add(substring)
    return list(result)