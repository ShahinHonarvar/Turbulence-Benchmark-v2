def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    lower_bound = 14
    upper_bound = 90
    min_length = 55
    max_length = 71
    palindromes = set()
    for length in range(min_length, max_length + 1):
        for i in range(lower_bound, upper_bound - length + 2):
            substring = s.lower()[i:i + length]
            if all((c.isalpha() for c in substring)) and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes