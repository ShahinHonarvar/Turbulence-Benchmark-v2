def all_substring_of_size_n(s):
    result = set()
    start, end = (0, len(s) - 90 + 1)
    while end <= len(s):
        substring = s[start:end]
        if len(substring) == 90 and len(set(substring)) == 90:
            result.add(substring)
        start += 1
        end += 1
    return list(result)