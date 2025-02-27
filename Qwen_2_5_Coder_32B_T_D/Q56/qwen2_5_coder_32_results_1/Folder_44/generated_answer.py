def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 89):
        substr = s[i:i + 90]
        if len(set(substr)) == 90:
            result.add(substr)
    return list(result)