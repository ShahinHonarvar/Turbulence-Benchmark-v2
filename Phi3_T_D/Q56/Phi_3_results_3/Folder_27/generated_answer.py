def all_substring_of_size_n(s):
    results = set()
    for i in range(len(s) - 56):
        substr = s[i:i + 57]
        if len(set(substr)) == 57:
            results.add(substr)
    return list(results)