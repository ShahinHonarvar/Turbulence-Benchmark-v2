def palindrome_of_length_n(s):
    s = s.lower()
    n = 88
    result = set()
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if all((c.isalpha() for c in substr)) and substr == substr[::-1]:
            result.add(substr)
    return result