def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 96):
        substring = s[i:i + 97]
        if len(set(substring)) == 97 and substring not in result:
            result.append(substring)
    return result