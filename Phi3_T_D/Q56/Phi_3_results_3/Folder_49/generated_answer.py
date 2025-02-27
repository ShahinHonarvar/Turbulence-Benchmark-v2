def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 72):
        if len(set(s[i:i + 73])) == 73:
            result.add(s[i:i + 73])
    return list(result)