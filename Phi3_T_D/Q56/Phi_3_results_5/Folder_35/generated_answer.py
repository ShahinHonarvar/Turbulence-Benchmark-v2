def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 26):
        substring = s[i:i + 27]
        if len(substring) == 27 and len(set(substring)) == 27:
            result.add(substring)
    return list(result)