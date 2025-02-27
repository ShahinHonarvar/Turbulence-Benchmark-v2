def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 126):
        substring = s[i:i + 127]
        if len(set(substring)) == 127:
            result.add(substring)
    return list(result)