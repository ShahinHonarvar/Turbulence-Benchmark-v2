def palindrome_of_length_n(s):

    def is_palindrome(substr):
        return substr.lower() == substr[::-1].lower()
    length = 88
    palindromes = set()
    for i in range(len(s) - length + 1):
        candidate = s[i:i + length]
        if is_palindrome(candidate):
            palindromes.add(candidate)
    return palindromes