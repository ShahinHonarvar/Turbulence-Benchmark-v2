def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 84):
        substring = s[i:i + 85]
        if len(substring) == 85 and len(set(substring)) == 85:
            result.append(substring)
    return result