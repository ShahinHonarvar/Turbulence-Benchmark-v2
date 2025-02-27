def palindromes_of_specific_lengths(input_string):

    def is_palindrome(s):
        return s == s[::-1]

    def valid_character(s):
        return s.isalpha() and s.isascii()
    palindromes = set()
    for length in range(37, 61):
        for i in range(11, 84 - length + 2):
            substring = input_string[i:i + length].lower()
            if all((valid_character(c) for c in substring)) and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes