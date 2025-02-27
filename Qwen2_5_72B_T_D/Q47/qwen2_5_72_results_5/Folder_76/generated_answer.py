def palindromes_of_specific_lengths(input_string):

    def is_palindrome(s):
        return s == s[::-1]
    substring = input_string[101:293]
    valid_palindromes = set()
    for length in range(154, 183):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate.isalpha() and is_palindrome(candidate.lower()):
                valid_palindromes.add(candidate)
    return valid_palindromes