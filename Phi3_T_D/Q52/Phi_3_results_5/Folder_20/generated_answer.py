def palindrome_of_length_n(s):
    results = set()
    str_lower = s.lower()
    for i in range(len(str_lower) - 52):
        substr = str_lower[i:i + 53].replace(' ', '')
        if substr == substr[::-1]:
            results.add(substr)
    return results