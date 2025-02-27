def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 69):
        substring = s[i:i + 70]
        if len(set(substring)) == 70:
            result.add(substring)
    return list(result)