def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 93):
        substring = s[i:i + 94]
        if len(set(substring)) == 94:
            result.add(substring)
    return list(result)