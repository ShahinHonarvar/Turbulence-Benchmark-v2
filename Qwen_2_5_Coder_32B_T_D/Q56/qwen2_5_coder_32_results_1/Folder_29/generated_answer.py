def all_substring_of_size_n(s):
    result = set()
    i = 0
    while i <= len(s) - 95:
        substring = s[i:i + 95]
        if len(set(substring)) == 95:
            result.add(substring)
        i += 1
    return list(result)