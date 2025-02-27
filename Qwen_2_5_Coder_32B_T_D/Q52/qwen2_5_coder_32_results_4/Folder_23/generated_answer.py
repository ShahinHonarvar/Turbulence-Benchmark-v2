def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 68):
        substr = s[i:i + 69]
        if substr.isalpha() and substr == substr[::-1]:
            result.add(substr)
    return result