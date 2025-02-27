def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 77):
        substring = s[i:i + 78]
        if len(set(substring)) == 78:
            result.add(substring)
    return list(result)