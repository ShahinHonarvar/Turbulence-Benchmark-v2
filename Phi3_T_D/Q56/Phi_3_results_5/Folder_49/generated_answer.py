def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 72):
        substring = s[i:i + 73]
        if len(set(substring)) == 73:
            result.append(substring)
    return result