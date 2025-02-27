def palindromes_of_specific_lengths(s):
    start = 30
    end = 95
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def valid_characters(char):
        return char in alphabet
    for length in range(34, 56):
        for i in range(start, end - length + 2):
            substring = s[i:i + length].lower()
            if all((valid_characters(char) for char in substring)) and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes