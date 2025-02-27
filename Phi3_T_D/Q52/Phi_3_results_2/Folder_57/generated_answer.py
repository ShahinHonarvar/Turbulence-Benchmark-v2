def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 83):
        substr = s[i:i + 92]
        if substr == substr[::-1]:
            result.add(substr.lower())
    return result