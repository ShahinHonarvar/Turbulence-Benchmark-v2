def all_substring_of_size_n(s):
    result = []
    length = len(s)
    for i in range(length - 19):
        substring = s[i:i + 20]
        if len(set(substring)) == 20:
            result.append(substring)
    return list(set(result))