def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 53):
        substr = s[i:i + 54]
        if substr == substr[::-1]:
            result.add(substr)
    return result