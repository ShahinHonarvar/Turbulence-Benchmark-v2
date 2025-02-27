def palindrome_of_length_n(s):
    s = s.lower()
    result_set = set()
    if len(s) < 45:
        return result_set
    for i in range(len(s) - 44):
        substr = s[i:i + 45]
        if substr == substr[::-1]:
            result_set.add(substr)
    return result_set