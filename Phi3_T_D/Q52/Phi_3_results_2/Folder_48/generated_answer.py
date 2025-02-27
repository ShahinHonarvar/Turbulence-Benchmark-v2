def palindrome_of_length_n(s):
    result = set()
    s_lower = s.lower()
    for i in range(len(s_lower) - 185):
        substr = s_lower[i:i + 186]
        if substr == substr[::-1] and substr.isalpha():
            result.add(s[i:i + 186].lower())
    return result