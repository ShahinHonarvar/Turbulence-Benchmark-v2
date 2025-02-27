def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def is_valid_char(char):
        return 'a' <= char <= 'z'
    palindromes = set()
    for length in range(154, 183):
        for i in range(101, 293 - length + 1):
            substring = s[i:i + length]
            if all((is_valid_char(char) for char in substring)) and is_palindrome(substring.lower()):
                palindromes.add(substring.lower())
    return palindromes