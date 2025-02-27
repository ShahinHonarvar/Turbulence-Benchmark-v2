def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 11):
        substring = s[i:i + 12]
        if len(set(substring)) == 12:
            result.add(substring)
    return list(result)