def palindrome_of_length_at_least_n(input_string):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    input_string = input_string.lower()
    n = 15
    for i in range(len(input_string) - n + 1):
        substring = input_string[i:i + n]
        if all((c.isalpha() for c in substring)) and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes