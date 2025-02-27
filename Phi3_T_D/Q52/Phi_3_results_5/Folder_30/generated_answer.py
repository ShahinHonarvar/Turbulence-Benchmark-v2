def palindrome_of_length_n(s):
    s = s.lower()
    result = set()

    def is_palindrome(substr):
        return substr == substr[::-1]
    for i in range(len(s) - 93):
        if is_palindrome(s[i:i + 94]):
            result.add(s[i:i + 94])
    return result