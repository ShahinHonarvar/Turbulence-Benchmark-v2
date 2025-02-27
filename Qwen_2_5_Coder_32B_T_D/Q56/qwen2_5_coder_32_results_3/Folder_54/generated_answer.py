def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 27):
        substring = s[i:i + 28]
        if len(set(substring)) == 28:
            result.add(substring)
    return list(result)