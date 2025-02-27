def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    n = 67
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if substr.isalpha() and substr == substr[::-1]:
            result.add(substr)
    return result