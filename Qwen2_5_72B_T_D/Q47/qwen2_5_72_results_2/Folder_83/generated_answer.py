def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    specified_substring = s[75:96]
    palindromes = set()
    for length in range(7, 10):
        for start in range(len(specified_substring) - length + 1):
            substring = specified_substring[start:start + length]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring.lower())
    return palindromes