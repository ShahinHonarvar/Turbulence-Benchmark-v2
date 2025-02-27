def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    substring = s[10:75]
    valid_palindromes = set()
    for length in range(6, 9):
        for start in range(len(substring) - length + 1):
            potential_palindrome = substring[start:start + length]
            if is_palindrome(potential_palindrome.lower()) and potential_palindrome.isalpha():
                valid_palindromes.add(potential_palindrome)
    return valid_palindromes