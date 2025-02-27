def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    n = len(s)
    for i in range(n - 275):
        substr = s[i:i + 276]
        if substr == substr[::-1]:
            result.add(substr.upper())
    return result