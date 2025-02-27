def palindrome_of_length_n(s):
    s = s.lower()

    def is_palindrome(substr):
        return substr == substr[::-1]
    length = 366
    result = set()
    for i in range(len(s) - length + 1):
        substr = s[i:i + length]
        if is_palindrome(substr) and substr.isalpha():
            result.add(substr.upper())
    return result