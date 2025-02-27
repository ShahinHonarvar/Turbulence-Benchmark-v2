def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def palindromes_of_specific_lengths(input_string):
    palindromes = set()
    for length in range(39, 53):
        for i in range(16, 95 - length + 1):
            substring = input_string[i:i + length]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes