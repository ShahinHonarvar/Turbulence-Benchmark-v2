def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]

    def is_valid_length(substr):
        return 31 <= len(substr) <= 51

    def is_alpha(substr):
        return substr.isalpha()
    upper_s = s.upper()
    relevant_s = upper_s[18:98]
    palindromes = set()
    for length in range(31, 52):
        for i in range(len(relevant_s) - length + 1):
            substr = relevant_s[i:i + length]
            if is_palindrome(substr) and is_valid_length(substr) and is_alpha(substr):
                palindromes.add(substr)
    return palindromes