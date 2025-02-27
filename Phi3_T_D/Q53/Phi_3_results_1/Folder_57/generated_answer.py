def palindrome_of_length_at_least_n(input_string):
    input_string = input_string.lower()

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    n = 93
    for i in range(len(input_string) - n + 1):
        substring = input_string[i:i + n]
        if all((char in alphabet for char in substring)) and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes