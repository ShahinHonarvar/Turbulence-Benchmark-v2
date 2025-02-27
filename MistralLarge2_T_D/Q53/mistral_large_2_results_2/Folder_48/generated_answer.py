def palindrome_of_length_at_least_n(input_string):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    input_string = ''.join(filter(str.isalpha, input_string.lower()))
    for length in range(150, len(input_string) + 1):
        for i in range(len(input_string) - length + 1):
            substr = input_string[i:i + length]
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes