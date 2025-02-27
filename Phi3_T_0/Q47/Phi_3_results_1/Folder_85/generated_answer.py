def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def valid_char(c):
        return 'a' <= c <= 'z'
    palindromes = set()
    for length in range(6, 10):
        for i in range(29, 99 - length + 1):
            substring = s[i:i + length]
            if all((valid_char(c) for c in substring)) and is_palindrome(substring.lower()):
                palindromes.add(substring.lower())
    return palindromes