def palindrome_of_length_n(input_string):

    def is_palindrome(s):
        return s == s[::-1]
    input_string = input_string.lower()
    palindromes = set()
    for i in range(len(input_string) - 278):
        substring = input_string[i:i + 279]
        if substring.isalpha() and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes