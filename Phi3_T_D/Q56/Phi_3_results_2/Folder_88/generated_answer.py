def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 67):
        substring = s[i:i + 68]
        if len(set(substring)) == 68:
            result.add(substring)
    return list(result)