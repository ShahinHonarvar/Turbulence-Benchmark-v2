def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 2):
        substring = s[i:i + 3]
        if len(set(substring)) == 3:
            result.append(substring)
    return list(set(result))