def palindrome_of_length_n(input_string):
    input_string = input_string.lower()
    length = 46
    palindromes = set()

    def is_palindrome(s):
        return s == s[::-1]
    for i in range(len(input_string) - length + 1):
        substring = input_string[i:i + length]
        if all((c.isalpha() for c in substring)):
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes