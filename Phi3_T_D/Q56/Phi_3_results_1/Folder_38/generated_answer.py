def all_substring_of_size_n(s):
    n = len(s)
    result = []
    for i in range(n - 34):
        substring = s[i:i + 35]
        if len(set(substring)) == 35:
            if substring not in result:
                result.append(substring)
    return result