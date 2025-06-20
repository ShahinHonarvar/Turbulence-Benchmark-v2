def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 66):
        substring = s[i:i + 67]
        if len(set(substring)) == 67:
            result.add(substring)
    return list(result)