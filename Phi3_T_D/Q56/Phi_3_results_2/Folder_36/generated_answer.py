def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 145):
        substring = s[i:i + 146]
        if len(set(substring)) == 146:
            result.add(substring)
    return list(result)