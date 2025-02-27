def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 89):
        substring = s[i:i + 90]
        if len(set(substring)) == 90:
            result.add(substring)
    return list(result)