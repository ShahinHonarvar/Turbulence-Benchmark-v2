def palindromes_of_specific_lengths(input_string):

    def is_palindrome(s):
        return s == s[::-1]
    substring = input_string[24:85]
    palindromes = set()
    for palindrome_length in range(21, 32):
        for start_index in range(0, len(substring) - palindrome_length + 1):
            candidate = substring[start_index:start_index + palindrome_length]
            if candidate.isalpha() and is_palindrome(candidate.lower()):
                palindromes.add(candidate)
    return palindromes